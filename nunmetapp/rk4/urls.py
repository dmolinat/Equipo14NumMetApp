from django.urls import path
from .views import RK4Create, RK4List, RK4Update

urlpatterns = [
    path('rk4s/', RK4List.as_view(), name ='rk4s'),
    path('rk4_create/', RK4Create.as_view(), name ='rk4-create'),
    path('rk4_update/<int:pk>/', RK4Update.as_view(), name ='rk4-update'),
]