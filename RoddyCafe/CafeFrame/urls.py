from django.urls import path
from . import views

urlpatterns = [
	path('', views.lobby, name='RoddyCafe_lobby'),
]