from django.urls import path, re_path, include
from . import views

urlpatterns= [
    path('persona/', views.index,name='inicio_app'),
    path('create_persona', views.create_person),
    path('person/<int:id>/', views.detail_person),
    path('delete_Person/<int:id>/', views.delete_person),
    path('update_Person/<int:id>/', views.update_person),
    path('evento/', views.index,name='evento_app'),
    path('opciones/', views.index,name='opciones_app')
]



