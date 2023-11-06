from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import NumericalMethod

    
"""Vistas para los elementos de methods"""
class MethodsList(LoginRequiredMixin, ListView):
    model = NumericalMethod
    context_object_name ='methods'
    ordering = ['date_use']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['methods'] = list(context['methods'].filter(user=self.request.user))[::-1]
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['methods'] = context['methods'].filter(
                date__startswith=search_input)
        return context

class MethodsDelete(LoginRequiredMixin, DeleteView):
    model = NumericalMethod
    fields = '__all__'
    success_url = reverse_lazy('home')