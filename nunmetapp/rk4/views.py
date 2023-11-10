from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .models import Rk4
from methods_app.models import NumericalMethod
from .utils.RK4 import RK4
import datetime


class RK4Create(LoginRequiredMixin, CreateView):
    model = Rk4
    fields = ['ED', 'a', 'b','Z','M']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        ED = form.cleaned_data['ED']        
        a = float(form.cleaned_data['a'])
        b = float(form.cleaned_data['b'])
        Z = float(form.cleaned_data['Z'])
        M = int(form.cleaned_data['M'])
        
        # Realiza el cálculo jacobi aquí y obtén los resultados
        (X,kind) = RK4(ED,a,b,Z,M)

        # Crea una instancia de boolerlOutput con los resultados y otros datos necesarios
        rk4_obj = Rk4(
            user=self.request.user,
                ED=ED,
                a=a,
                b=b,
                Z=Z,
                M=M,
                
                X=X,
                kind=kind,
        )
        rk4_obj.save()
        methods=NumericalMethod(
            user=self.request.user,
            inputs={
                'ED':ED,
                'a':a,
                'b':b,
                'Z':Z,
                'M':M,
            },
            outputs={
                'X':X,
                'kind':kind,
            },
            kind="RK4",
            rk4=rk4_obj,
            date_use=datetime.datetime.today()
        )
        methods.save()
        return redirect('home')

class RK4List(LoginRequiredMixin, ListView):
    model = Rk4
    context_object_name ='rk4s'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rk4s'] = list(context['rk4s'].filter(user=self.request.user))[::-1]  
        return context
    
class RK4Update(LoginRequiredMixin, UpdateView):
    model = Rk4
    fields = ['ED', 'a', 'b','Z','M']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        rk4_id=self.object.id
        rk4_output=Rk4.objects.get(id=rk4_id)
        
        ED = form.cleaned_data['ED']        
        a = float(form.cleaned_data['a'])
        b = float(form.cleaned_data['b'])
        Z = float(form.cleaned_data['Z'])
        M = int(form.cleaned_data['M'])
        
        (X,kind) = RK4(ED,a,b,Z,M)
                
        rk4_output.ED=ED
        rk4_output.a=a
        rk4_output.b=b
        rk4_output.Z=Z
        rk4_output.M=M
        
        rk4_output.X=X
        rk4_output.kind=kind
        
        rk4_output.save()
        
        method_updated=NumericalMethod.objects.get(rk4=rk4_id)
        method_updated.inputs={
                'ED':ED,
                'a':a,
                'b':b,
                'Z':Z,
                'M':M,
            }
        method_updated.outputs={
                'X':X,
                'kind':kind,
            }
        method_updated.kind=kind
        method_updated.date_use=datetime.datetime.today()
        method_updated.save()
        return redirect('home')        
