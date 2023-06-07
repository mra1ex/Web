from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='general'),
    path('singin', views.singin, name='singin'),
    path('singup/', views.singup, name='singup'),
    path('main/', views.general1, name='general1'),
    path('create/', views.create, name='create')
]


