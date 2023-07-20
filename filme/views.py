from typing import Any, Dict
from django import http
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomePage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# def homepage(request):
#     return render(request, "homepage.html")


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomePage

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            return redirect("filme:homefilmes")
        else:
            return super().get(request, *args, **kwargs)  # re-direciona para Homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse( 'filme:login')
        else:
            return reverse( 'filme:criarconta')


# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data()
        filmes_relacionados = self.model.objects.filter(
            categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        # que filme o usuario esta a acessando?
        filme = self.get_object()
        filme.vizualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_visualizados.add(filme)
        return super().get(request, *args, **kwargs)


class Pesquisa_filme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(
                titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields =["first_name","last_name","email"]

    def get_success_url(self):
        return reverse('filme:homefilmes')


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm


    def form_valid(self, form: Any):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')
