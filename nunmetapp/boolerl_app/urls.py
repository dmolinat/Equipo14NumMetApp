from django.urls import path
from .views import BoolerlOutputCreate, BoolerlOutputList, BoolerlOutputUpdate

urlpatterns = [
    path('booleroutputs/', BoolerlOutputList.as_view(), name ='boolerloutputs'),
    path('boolerloutput_create/', BoolerlOutputCreate.as_view(), name ='boolerloutput-create'),
    path('boolerloutput_update/<int:pk>/', BoolerlOutputUpdate.as_view(), name ='boolerloutput-update'),
]