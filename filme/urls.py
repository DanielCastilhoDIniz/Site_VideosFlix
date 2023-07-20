from django.contrib import admin
from django.urls import path, reverse_lazy
from filme import views
from django.contrib.auth import views as auth_view

app_name = 'filme'

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('filmes/', views.Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', views.Detalhesfilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', views.Pesquisa_filme.as_view(), name='pesquisa_filme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>',  views.PaginaPerfil.as_view(template_name='editarperfil.html'), name='editarperfil'),
    path('criarconta/',  views.CriarConta.as_view(template_name='criarconta.html'), name='criarconta'),
    path('mudarsenha/',auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]
