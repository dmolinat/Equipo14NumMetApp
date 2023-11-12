from django.urls import path
from .views import create_cookie_method, confirm_cookie
urlpatterns = [
    path('methodcount_create/', create_cookie_method, name ='create-cookie-method'),
    path('cookie_confirmation/', confirm_cookie, name ='confirm-cookie'),
]