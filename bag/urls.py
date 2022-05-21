from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='bag'),
    path('add/<box_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<box_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<box_id>/', views.remove_from_bag, name='remove_from_bag'),
]
