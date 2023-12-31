from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render

from cookie.views import start_cookie

def home(request):
    return render(request, 'index.html')

class CustomLoginView(LoginView):
    start_cookie()
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('confirm-cookie')

class RegisterPage(FormView):
    start_cookie()
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('confirm-cookie')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
         return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)
