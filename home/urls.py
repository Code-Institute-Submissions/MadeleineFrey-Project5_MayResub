from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.team, name='about_us'),
    path('addt/', views.add_team, name='add_team'),
    path('addl/', views.add_location, name='add_location'),
    path('addc/', views.add_contact, name='add_contact'),
    path('editt/<int:member_id>/', views.edit_team, name='edit_team'),
    path('editc/<int:member_id>/', views.edit_contact, name='edit_contact'),
    path('editl/<int:location_id>/', views.edit_location, name='edit_location'),
    

]