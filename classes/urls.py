from django.urls import path
from . import views

urlpatterns = [
    #path del classes
    path('', views.classes, name="classes"),
    path('<int:class_id>/', views.clase, name="clase"),
]