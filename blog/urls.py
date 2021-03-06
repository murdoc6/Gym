from django.urls import path
from . import views

urlpatterns = [
    #path del blog
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
    path('<int:post_id>/', views.post, name="post"),
]