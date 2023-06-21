from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='general'),
    path('singin', views.signin, name='signin'),
    path('singup/', views.signup, name='signup'),
    path('main/', views.general1, name='general1'),
    # path('create/', views.create, name='create')
]


