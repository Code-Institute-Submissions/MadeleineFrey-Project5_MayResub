from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_boxes, name='boxes'),
    path('<int:box_id>/', views.detail_box, name='box_detail'),
    path('add/', views.add_box, name='add_box'),
    path('edit/<int:box_id>/', views.edit_box, name='edit_box'),
    path('delete/<int:box_id>/', views.delete_box, name='delete_box'),
]
