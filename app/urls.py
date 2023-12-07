from django.urls import path, re_path, include
from . import views

urlpatterns= [
    path('Person/', views.index,name='inicio_app'),
    path('Evento/', views.index,name='evento_app'),
    path('Opciones/', views.index,name='opciones_app')
]




