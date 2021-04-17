# users\urls.py

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Home page
    path('', include('django.contrib.auth.urls')),
    # Registration site
    path('register/', views.register, name='register')
]
