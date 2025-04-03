from django.urls import path
from .views import get_categories, create_category, update_category, delete_category

urlpatterns = [
    path('categories/', get_categories, name='get_categories'),
    path('create-category/', create_category, name='create_category'),
    path('update-category/<int:id>/', update_category, name='update_category'),
    path('delete-category/<int:id>/', delete_category, name='delete_category')
]
