from django.urls import path
from .views import JacobiCreate, JacobiList

urlpatterns = [
    path('jacobis/', JacobiList.as_view(), name ='jacobis'),
    path('jacobi_create/', JacobiCreate.as_view(), name ='jacobi-create'),
]