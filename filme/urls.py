from django.contrib import admin
from django.urls import path
from filme import views


urlpatterns = [
        path('', views.Homepage.as_view() ),
        path('filmes/', views.Homefilmes.as_view())
        ]