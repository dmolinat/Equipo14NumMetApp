from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import NumericalMethod

    
"""Vistas para los elementos de methods"""
class MethodsList(LoginRequiredMixin, ListView):
    model = NumericalMethod
    context_object_name ='methods'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['methods'] = list(context['methods'].filter(user=self.request.user))[::-1]
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['methods'] = context['methods'].filter(
                date__startswith=search_input)
        return context

class methodsDetail(LoginRequiredMixin, DetailView):
    model = MethodsList
    context_object_name ='methodslist'
    template_name = 'base/methods.html'