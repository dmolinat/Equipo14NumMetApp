from django.urls import path
from .views import MethodsDelete,MethodsList, HelpMethods
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',MethodsList.as_view(), name='home'),
    path('methods_delete/<int:pk>/', MethodsDelete.as_view(), name ='methods-delete'),
    path('methods_help/', HelpMethods, name ='help'),
]