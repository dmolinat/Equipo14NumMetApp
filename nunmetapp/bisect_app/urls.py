from django.urls import path
from .views import BisectOutputList,BisectOutputCreate, BisectOutputUpdate, help_buttom_bisect
urlpatterns = [
    path('bisectoutputs/', BisectOutputList.as_view(), name ='bisectoutputs'),
    path('bisectoutput_create/', BisectOutputCreate.as_view(), name ='bisectoutput-create'),
    path('bisectoutput_update/<int:pk>/', BisectOutputUpdate.as_view(), name ='bisectoutput-update'),
    path('hello_world_bisect/', help_buttom_bisect, name='hello_world'),
]