from django.contrib import admin
from django.urls import path
from filme import views

app_name= 'filme'

urlpatterns = [
        path('', views.Homepage.as_view(), name='homepage' ),
        path('filmes/', views.Homefilmes.as_view(), name='homefilmes'),
        path('filmes/<int:pk>', views.Detalhesfilme.as_view(), name='detalhesfilme')
        ]