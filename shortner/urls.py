from django.urls import path
from .views import hello, creatingUrl,redirect,showAll

urlpatterns = [
    path('', hello, name='home'),
    path('create/', creatingUrl, name='create'),
    path('<str:url>', redirect, name='redirect'),
     path('showAll/', showAll, name='showAll'),

]