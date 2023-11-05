from django.urls import path
from .views import BoolerlOutputCreate, BoolerlOutputList

urlpatterns = [
    path('booleroutputs/', BoolerlOutputList.as_view(), name ='boolerloutputs'),
    path('boolerloutput_create/', BoolerlOutputCreate.as_view(), name ='boolerloutput-create'),
]