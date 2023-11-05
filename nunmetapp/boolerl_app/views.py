from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .models import BoolerlOutput
from methods_app.models import NumericalMethod
from .utils.boolerl import boolerl


class BoolerlOutputCreate(LoginRequiredMixin, CreateView):
    model = BoolerlOutput
    fields = ['f_s', 'a', 'b','M']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        f_s = form.cleaned_data['f_s']        
        a = int(form.cleaned_data['a'])
        b = int(form.cleaned_data['b'])
        M= int(form.cleaned_data['M'])
        
        # Realiza el cálculo boolerl aquí y obtén los resultados
        (aprox, kind) = boolerl(f_s,a,b,M)

        # Crea una instancia de boolerlOutput con los resultados y otros datos necesarios
        boolerl_output = BoolerlOutput(
            user=self.request.user,
                a=a,
                b=b,
                f_s=f_s,
                M=M,
                aprox=aprox,
                kind=kind,
        )
        boolerl_output.save()
        methods=NumericalMethod(
            user=self.request.user,
            inputs={
                "f_s":f_s,
                "a":a,
                "b":b,
                "M":M
            },
            outputs={
                "aprox":aprox,
                "kind":kind
            },
            kind="BOOLERL",
        )
        methods.save()
        return redirect('home')

class BoolerlOutputList(LoginRequiredMixin, ListView):
    model = BoolerlOutput
    context_object_name ='boolerloutputs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boolerloutputs'] = list(context['boolerloutputs'].filter(user=self.request.user))[::-1]
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['boolerloutputs'] = context['boolerloutputs'].filter(
                date__startswith=search_input)
        return context
