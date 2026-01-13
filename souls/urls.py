from django.urls import path
from . import views

urlpatterns = [
    path('', views.graveyard_welcome, name='home'),
]