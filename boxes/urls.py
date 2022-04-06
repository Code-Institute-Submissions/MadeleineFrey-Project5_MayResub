from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_boxes, name='boxes'),
    path('<box_id>', views.detail_box, name='box_detail'),
]
