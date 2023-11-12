from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import NumericalMethod
from cookie.models import CookieCountMethodUse
    
"""Vistas para los elementos de methods"""
class MethodsList(LoginRequiredMixin, ListView):
    model = NumericalMethod
    context_object_name ='methods'
    ordering = ['date_use']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['methods'] = list(context['methods'].filter(user=self.request.user))[::-1]
        
        context['bisect_count'] = CookieCountMethodUse.objects.get(method="BISECT").count
        context['jacobi_count'] = CookieCountMethodUse.objects.get(method="JACOBI").count
        context['boolerl_count'] = CookieCountMethodUse.objects.get(method="BOOLERL").count
        context['rk4_count'] = CookieCountMethodUse.objects.get(method="RK4").count
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['methods'] = context['methods'].filter(
                date__startswith=search_input)
        return context

class MethodsDelete(LoginRequiredMixin, DeleteView):
    model = NumericalMethod
    fields = '__all__'
    success_url = reverse_lazy('home')
    
def HelpMethods(request):
    return render(request, 'methods_app/help.html')