from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .models import Jacobi
from methods_app.models import NumericalMethod
from .utils.jacobi import jacobi


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
        
        # Realiza el cálculo boolerl aquí y obtén los resultados
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
        )
        methods.save()
        return redirect('home')

class JacobiList(LoginRequiredMixin, ListView):
    model = Jacobi
    context_object_name ='jacobis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jacobis'] = list(context['jacobis'].filter(user=self.request.user))[::-1]  
        return context
