from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('methods_app.urls')),
    path('',include('boolerl_app.urls')),
    path('', include('user.urls')),
    path('', include('bisect_app.urls')),
    path('', include('jacobi.urls')),
]
