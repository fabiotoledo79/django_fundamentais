"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contas.views import home, listagem, nova_transacao, update_transacao, delete_transacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('', listagem, name='listagem_transacao_path'),
    path('nova/', nova_transacao, name='nova_transacao_path'),
    path('update/<int:pk>/', update_transacao, name='update_transacao_path'),
    path('delete/<int:pk>/', delete_transacao, name='delete_transacao_path')
]
