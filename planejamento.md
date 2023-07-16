<h2>Elementos do site:</h2>

<h3>Homepage</h3>

<h3>Fazer Login e Criar Conta (Usuário e Autenticação)</h3>
<ul>
  <li>Email</li>
  <li>Username</li>
  <li>Senha</li>
  <li>Filmes já vistos</li>
  <li>Editar Perfil</li>
</ul>

<h3>Filmes/Séries</h3>
<ul>
  <li>thumb</li>
  <li>titulo</li>
  <li>descrição</li>
  <li>categoria</li>
  <li>quantidade de views</li>
  <li>data de criação</li>
  <li>Episódios</li>
  <ul>
    <li>videos</li>
    <li>titulo</li>
  </ul>
</ul>

<h3>Barra de Pesquisa</h3>

<ol>
   <li>1° passo - Criar ambiente virtual: <code>python -m venv dev_django</code>.<br>
   - Ativar ambiente virtual: <code>. dev_django\Scripts\activate.ps1</code>.</li>
   <li>2° passo - Escolher diretório para criar o projeto.</li>
   <li>3° passo - Começar projeto com o comando: <code>django-admin startproject nome_do_projeto</code>.</li>
   <li>4° passo - Criar app: <code>django-admin startapp nome_do_app</code>.</li>
   <li>5° passo - Criar superuser:<br>
   - Migrar banco de dados: <code>python manege.py migrate</code>.<br>
   - Criar superusuário: <code>django-admin mange.py createsuperuser</code>.</li>
   <li>6° passo - Integrar app com projeto - Ir até o arquivo settings.py:<br>
   - <strong>INSTALLED_APPS:</strong><br>
   <pre>
   INSTALLED_APPS = [
       'nome_do_app'
   ]</pre>
   - <strong>Internationalization:</strong><br>
   <pre>
   LANGUAGE_CODE = 'pt-bt'
   TIME_ZONE = 'America/Sao_Paulo'
   USE_I18N = True
   USE_TZ = True</pre>
   </li>
   <li>7° passo - Criar classes em models.py:<br>
   - Cada elemento da tabela é criado.<br>
   - Comando:<br>
   <code>python manage.py makemigrations</code><br>
   <code>python manage.py migrate</code></li>
   <li>8° passo - Criar a pasta static e as subpastas css, js e Images:<br>
   - No arquivo settings.py, ajustar:<br>
   <strong>STATIC_URL:</strong> 'static/'<br>
   <strong>STATICFILES_DIRS:</strong><br>
   <pre>
   STATICFILES_DIRS = [
       BASE_DIR / "static",
   ]</pre>
   - No arquivo do urls.py do projeto, adicionar ao urlpatterns a linha:<br>
   <code>+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)</code><br>
   - Importar as bibliotecas:<br>
   <code>from django.conf import settings</code><br>
   <code>from django.conf.urls.static import static</code></li>
   <li>9° passo - Ajustar arquivos de mídia:<br>
   - Criar a pasta mídia.<br>
   - Definir em settings.py:<br>
   <strong>MEDIA_URL:</strong> ...<br>
   <strong>MEDIA_ROOT:</strong> ...<br>
   - Na pasta urls.py do projeto, adicionar ao urlpatterns a linha:<br>
   <code>+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)</code></li>
   <li>10° passo - Criar a pasta templates na raiz do projeto e adicionar no documento settings.py o nome 'templates' em 'DIRS':<br>
   <pre>
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': ['templates'],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]</pre>
   - Esta será a pasta de templates para toda aplicação.</li>
   <li>11° passo - Criar a pasta template dentro do app filme, nesta pasta terá um padrão para o app filme.</li>
   <li>12° passo - Criar na pasta template raiz, os modelos base HTML para navbar.html e base.html.</li>
   <li>13° passo - editar a base.html. colocando os blocos que se repetirão por toda aplicação, ajustar fazer o front da barra de navegação usado o bootstrap e o tailwindcss</li>
   <li>14° passo - Editar a homepage, criar divs, botões, inserir imagens, etc, front... atenção para a configurações do taiwind</li>
   <li>15° usnado o class como view: </li>
     - from django.views.generic import TemplateView, ListView, DetailView
    <li>16° passo - ajustar urls do app></li>:
    - urlpatterns = [
        path('', views.Homepage.as_view(), name='homepage' ),
        path('filmes/', views.Homefilmes.as_view(), name='homefilmes'),
        path('filmes/<int:pk>', views.Detalhesfilme.as_view(), name='detalhesfilme')
        ]
    <li>17° criar aquivo context.py ou novo_context.py inserir funções que retornam um lista na pagina html, ajustas setting.py  o 'context_processors': []></li>:
</ol>
