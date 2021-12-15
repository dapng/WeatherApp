from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('info', views.info, name='info')
]
