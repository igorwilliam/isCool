"""iscool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import login, logout

from core import views
from post import urls as post_urls
from accounts import urls as accounts_urls


urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('postar/',include(post_urls)),
    path('conta/',include(accounts_urls)),
    path('entrar/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('sair/', logout, {'next_page': 'login'}, name='logout'),

]
