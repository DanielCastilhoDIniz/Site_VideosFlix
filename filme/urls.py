from django.contrib import admin
from django.urls import path
from filme import views


urlpatterns = [
        path('', views.homepage ),
        path('filmes/', views.homefilmes)
        ]