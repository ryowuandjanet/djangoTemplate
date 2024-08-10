from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/update/<int:pk>/', views.article_update, name='article_update'),
    path('article/update/form/<int:pk>/', views.article_update_form, name='article_update_form'),  # Add this line
    path('article/delete/<int:pk>/', views.article_delete, name='article_delete'),
]
