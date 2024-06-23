from django.urls import path
from .views import user_view

urlpatterns = [
    path('user/', user_view, name='user_list_create'),
    path('user/<int:pk>/', user_view, name='user_detail_update_delete'),
]
