from django.urls import path
from .views import MethodsDelete,MethodsList, HelpMethods, HelpBisect, HelpBoolerl, HelpJacobi, HelpRK4

urlpatterns = [
    path('',MethodsList.as_view(), name='home'),
    path('methods_delete/<int:pk>/', MethodsDelete.as_view(), name ='methods-delete'),
    path('methods_help/', HelpMethods, name ='help'),
    path('bisect_help/', HelpBisect, name ='bisect-help'),
    path('boolerl_help/', HelpBoolerl, name ='boolerl-help'),
    path('jacobi_help/', HelpJacobi, name ='jacobi-help'),
    path('rk4_help/', HelpRK4, name ='rk4-help'),
]