
from django.urls import path
from . import views

urlpatterns = [
    path('', views.nested_home),
    path('about/', views.nested_about),
]
