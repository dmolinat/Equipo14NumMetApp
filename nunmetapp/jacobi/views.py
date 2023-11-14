from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .models import Jacobi
from methods_app.models import NumericalMethod
from .utils.jacobi import jacobi
import datetime

from cookie.models import UserCookie, CookieCountMethodUse


class JacobiCreate(LoginRequiredMixin, CreateView):
    model = Jacobi
    fields = ['A', 'B', 'x0','tolerance','max_iter']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        A = form.cleaned_data['A']        
        B = str(form.cleaned_data['B'])
        x0 = str(form.cleaned_data['x0'])
        tolerance = float(form.cleaned_data['tolerance'])
        max_iter = int(form.cleaned_data['max_iter'])
        
        # Realiza el cálculo jacobi aquí y obtén los resultados
        (X,number_iteration,err,kind) = jacobi(A,B,x0,tolerance,max_iter)

        # Crea una instancia de boolerlOutput con los resultados y otros datos necesarios
        jacobi_obj = Jacobi(
            user=self.request.user,
                A=A,
                B=B,
                x0=x0,
                tolerance=tolerance,
                max_iter=max_iter,
                
                X=X,
                number_iteration=number_iteration,
                err=err,
                kind=kind,
        )
        jacobi_obj.save()
        methods=NumericalMethod(
            user=self.request.user,
            inputs={
                'A':A,
                'B':B,
                'x0':x0,
                'tolerance':tolerance,
                'max_iter':max_iter,
            },
            outputs={
                'X':X,
                'number_iteration':number_iteration,
                'err':err,
                'kind':kind,
            },
            kind="JACOBI",
            jacobi=jacobi_obj,
            date_use=datetime.datetime.today()
        )
        methods.save()
        
        cookie_query=UserCookie.objects.filter(user=self.request.user)
        cookie_obj=cookie_query.order_by("date_use").last()
        if(cookie_obj.cookie_active==True):
            cookie_method_obj=CookieCountMethodUse.objects.get(method="JACOBI")
            cookie_method_obj.count+=1
            cookie_method_obj.save()
            
        return redirect('home')

class JacobiList(LoginRequiredMixin, ListView):
    model = Jacobi
    context_object_name ='jacobis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jacobis'] = list(context['jacobis'].filter(user=self.request.user))[::-1]  
        return context
    
class JacobiUpdate(LoginRequiredMixin, UpdateView):
    model = Jacobi
    fields = ['A', 'B', 'x0','tolerance','max_iter']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        jacobi_id=self.object.id
        jacobi_output=Jacobi.objects.get(id=jacobi_id)
        
        A = form.cleaned_data['A']        
        B = str(form.cleaned_data['B'])
        x0 = str(form.cleaned_data['x0'])
        tolerance = float(form.cleaned_data['tolerance'])
        max_iter = int(form.cleaned_data['max_iter'])
        
        
        # Realiza el cálculo jacobi aquí y obtén los resultados
        (X,number_iteration,err,kind) = jacobi(A,B,x0,tolerance,max_iter)
        
        jacobi_output.A=A
        jacobi_output.B=B
        jacobi_output.x0=x0
        jacobi_output.tolerance=tolerance
        jacobi_output.max_iter=max_iter
        
        jacobi_output.X=X
        jacobi_output.number_iteration=number_iteration
        jacobi_output.err=err
        jacobi_output.kind=kind
        
        jacobi_output.save()
        method_updated=NumericalMethod.objects.get(jacobi=jacobi_id)
        method_updated.inputs={
               'A':A,
                'B':B,
                'x0':x0,
                'tolerance':tolerance,
                'max_iter':max_iter,
            }
        method_updated.outputs={
                'X':X,
                'number_iteration':number_iteration,
                'err':err,
                'kind':kind,
            }
        method_updated.kind=kind
        method_updated.date_use=datetime.datetime.today()
        method_updated.save()
        
        cookie_query=UserCookie.objects.filter(user=self.request.user)
        cookie_obj=cookie_query.order_by("date_use").last()
        if(cookie_obj.cookie_active==True):
            cookie_method_obj=CookieCountMethodUse.objects.get(method="JACOBI")
            cookie_method_obj.count+=1
            cookie_method_obj.save()
            
        return redirect('home')        
