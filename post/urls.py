from django.urls import path
from .views import post_list_create, post_detail_delete

urlpatterns = [
    path('posts/', post_list_create),                  
    path('posts/<int:post_id>/', post_detail_delete),  
]
