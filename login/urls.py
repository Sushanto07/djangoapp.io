# LoginFormProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginapp/', include('loginapp.urls')),
]
