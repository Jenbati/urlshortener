from django.urls import path 
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create/', views.create_short_url, name="create"),
    path('<str:code>/', views.redirect_url, name="redirect"),
    path('delete/<int:id>/', views.delete_url, name="delete"),
]
