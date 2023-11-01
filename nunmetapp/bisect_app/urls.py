from django.urls import path
from .views import BisectOutputList,BisectOutputDetail,BisectOutputCreate,BisectOutputDelete

urlpatterns = [
    path('bisectoutputs/', BisectOutputList.as_view(), name ='bisectoutputs'),
    path('bisectoutput/<int:pk>/', BisectOutputDetail.as_view(), name ='bisectoutput'),
    path('bisectoutput_create/', BisectOutputCreate.as_view(), name ='bisectoutput-create'),
    path('bisectoutput_delete/<int:pk>/', BisectOutputDelete.as_view(), name ='bisectoutput-delete'),
]