from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .models import BisectOutput
from .utils.bisect import bisect
from methods_app.models import NumericalMethod
import datetime
from django.shortcuts import render
from cookie.models import UserCookie,CookieCountMethodUse

class BisectOutputCreate(LoginRequiredMixin, CreateView):
    model = BisectOutput
    fields = ['f_s', 'a', 'b','tolerance']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        f_s = form.cleaned_data['f_s']        
        a = int(form.cleaned_data['a'])
        b = int(form.cleaned_data['b'])
        tolerance= float(form.cleaned_data['tolerance'])
        
        # Realiza el cálculo bisect aquí y obtén los resultados
        (root, err, froot, kind) = bisect(f_s,a,b,tolerance)

        # Crea una instancia de BisectOutput con los resultados y otros datos necesarios
        bisect_output = BisectOutput(
            user=self.request.user,
                a=a,
                b=b,
                f_s=f_s,
                tolerance=tolerance,
                root=root,
                err=err,
                froot=froot,
                kind=kind,
        )
        bisect_output.save()
        methods=NumericalMethod(
            user=self.request.user,
            inputs={
                "f_s":f_s,
                "a":a,
                "b":b,
                "tolerance":tolerance
            },
            outputs={
                "root":root,
                "err": err,
                "froot":froot,
                "kind": kind,
            },
            kind="BISECT",
            bisect=bisect_output,
            date_use=datetime.datetime.today()
        )
        methods.save()
        cookie_query=UserCookie.objects.filter(user=self.request.user)
        cookie_obj=cookie_query.order_by("date_use").last()
        if(cookie_obj.cookie_active==True):
            cookie_method_obj=CookieCountMethodUse.objects.get(method=kind)
            cookie_method_obj.count+=1
            cookie_method_obj.save()

        return redirect('home')

class BisectOutputList(LoginRequiredMixin, ListView):
    model = BisectOutput
    context_object_name ='bisectoutputs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bisectoutputs'] = list(context['bisectoutputs'].filter(user=self.request.user))[::-1]
        return context

class BisectOutputUpdate(LoginRequiredMixin, UpdateView):
    model = BisectOutput
    fields = ['f_s', 'a', 'b','tolerance']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        bisect_id=self.object.id
        bisect_output=BisectOutput.objects.get(id=bisect_id)
        
        f_s = form.cleaned_data['f_s']        
        a = int(form.cleaned_data['a'])
        b = int(form.cleaned_data['b'])
        tolerance= float(form.cleaned_data['tolerance'])
        
        # Realiza el cálculo bisect aquí y obtén los resultados
        (root, err, froot, kind) = bisect(f_s,a,b,tolerance)
        
        bisect_output.f_s=f_s
        bisect_output.a=a
        bisect_output.b=b
        bisect_output.tolerance=tolerance
        bisect_output.root=root
        bisect_output.err=err
        bisect_output.froot=froot
        bisect_output.kind=kind
        
        bisect_output.save()
        method_updated=NumericalMethod.objects.get(bisect=bisect_id)
        method_updated.inputs={
            'f_s':f_s,
            'a':a,
            'b':b,
            'tolerance':tolerance,
        }
        method_updated.outputs={
            'root':root,
            'err':err,
            'froot':froot,
            'kind': kind
        }
        method_updated.kind=kind
        method_updated.date_use=datetime.datetime.today()
        method_updated.save()
        
        cookie_query=UserCookie.objects.filter(user=self.request.user)
        cookie_obj=cookie_query.order_by("date_use").last()
        if(cookie_obj.cookie_active==True):
            cookie_method_obj=CookieCountMethodUse.objects.get(method=kind)
            cookie_method_obj.count+=1
            cookie_method_obj.save()
        
        return redirect('home')
        
def help_buttom_bisect(request):
    show_message = request.session.get('show_message', False)
    if request.method == 'POST':
        # Cambia el estado del mensaje en función de su estado actual
        show_message = not show_message
        request.session['show_message'] = show_message
            
    return render(request, 'bisect_app/hello_world.html', {'show_message': show_message})