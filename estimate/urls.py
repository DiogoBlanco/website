from django.urls import path
from . import views

app_name = 'estimates'

urlpatterns = [
    path('', views.estimates, name='estimates')
]
