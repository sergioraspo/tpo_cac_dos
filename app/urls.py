from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('reserva/', views.index,name='inicio_app')
   
]
