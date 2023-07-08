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
</ol>
