from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .models import BisectOutput
from .utils.bisect import bisect

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
        (root, err, froot) = bisect(f_s,a,b,tolerance)

        # Crea una instancia de BisectOutput con los resultados y otros datos necesarios
        bisect_output = BisectOutput(
            user=self.request.user,
                a=a,
                b=b,
                f_s=f_s,
                tolerance=tolerance,
                root=root,
                err=err,
                froot=froot
        )
        bisect_output.save()
        return redirect('bisectoutputs')

class BisectOutputUpdate(LoginRequiredMixin, UpdateView):
    model = BisectOutput
    fields = ['f_s', 'a', 'b','tolerance']
    success_url = reverse_lazy('bisectoutputs')

class BisectOutputDelete(LoginRequiredMixin, DeleteView):
    model = BisectOutput
    fields = '__all__'
    success_url = reverse_lazy('home')
    
"""Vistas para los elementos de BisectOutput"""
class BisectOutputList(LoginRequiredMixin, ListView):
    model = BisectOutput
    context_object_name ='bisectoutputs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bisectoutputs'] = list(context['bisectoutputs'].filter(user=self.request.user))[::-1]
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['bisectoutputs'] = context['bisectoutputs'].filter(
                date__startswith=search_input)
        return context

class BisectOutputDetail(LoginRequiredMixin, DetailView):
    model = BisectOutput
    context_object_name ='bisectoutput'
    template_name = 'base/bisectoutput.html'