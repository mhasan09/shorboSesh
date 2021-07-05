from django.urls import path
from . import views

urlpatterns = [
    path('', views.sorboSesh, name='home'),


]