from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from .models import BisectOutput

class BisectOutputCreate(LoginRequiredMixin, CreateView):
    model = BisectOutput
    fields = ['f_s', 'root', 'err','froot']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BisectOutputCreate, self).form_valid(form)

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
        context['bisectoutputs'] = context['bisectoutputs'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['bisectoutputs'] = context['bisectoutputs'].filter(
                date__startswith=search_input)
        return context

class BisectOutputDetail(LoginRequiredMixin, DetailView):
    model = BisectOutput
    context_object_name ='bisectoutput'
    template_name = 'base/bisectoutput.html'