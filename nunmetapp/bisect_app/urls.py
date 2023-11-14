from django.urls import path
from .views import BisectOutputList,BisectOutputCreate, BisectOutputUpdate
urlpatterns = [
    path('bisectoutputs/', BisectOutputList.as_view(), name ='bisectoutputs'),
    path('bisectoutput_create/', BisectOutputCreate.as_view(), name ='bisectoutput-create'),
    path('bisectoutput_update/<int:pk>/', BisectOutputUpdate.as_view(), name ='bisectoutput-update'),
]