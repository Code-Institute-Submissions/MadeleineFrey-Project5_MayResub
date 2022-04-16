from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.team, name='about_us'),
    path('addt/', views.add_team, name='add_team'),
    path('addl/', views.add_location, name='add_location'),



]