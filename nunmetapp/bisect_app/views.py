from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .models import BisectOutput
from .utils.bisect import bisect
from methods_app.models import NumericalMethod

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
        )
        methods.save()
        return redirect('home')

class BisectOutputList(LoginRequiredMixin, ListView):
    model = BisectOutput
    context_object_name ='bisectoutputs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bisectoutputs'] = list(context['bisectoutputs'].filter(user=self.request.user))[::-1]
        return context