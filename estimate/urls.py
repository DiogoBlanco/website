from django.urls import path
from . import views

urlpatterns = [
    path('', views.estimates, name='estimates')
]
