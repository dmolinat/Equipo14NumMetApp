from django.urls import path
from .views import JacobiCreate, JacobiList, JacobiUpdate

urlpatterns = [
    path('jacobis/', JacobiList.as_view(), name ='jacobis'),
    path('jacobi_create/', JacobiCreate.as_view(), name ='jacobi-create'),
    path('jacobi_update/<int:pk>/', JacobiUpdate.as_view(), name ='jacobi-update'),
]