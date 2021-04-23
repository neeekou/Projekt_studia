"""baza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from strony import views
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Start, name='home/'),
    path('StronaGlowna', views.StronaGlowna, name='home/'),
    path('zakladanie_konta', views.zakladanie_konta, name='home/'),
    path('Statystyki', views.Statystyki, name='home/'),
    path('Roczniki', views.Roczniki, name='home/'),
    path('Regulamin', views.Regulamin, name='home/'),
    path('Projekt', views.Projekt, name='home/'),
    path('Omnie', views.Omnie, name='home/'),
    path('Kontakt', views.Kontakt, name='home/'),
    path('2020', views.P_2020, name='home/'),
    path('2019', views.P_2019, name='home/'),
    path('2018', views.P_2018, name='home/'),
    path('2017', views.P_2017, name='home/'),
    path('2016', views.P_2016, name='home/'),
    path('2015', views.P_2015, name='home/'),
    path('2014', views.P_2014, name='home/'),
    path('2013', views.P_2013, name='home/'),
    path('2021', views.P_2021, name='home/'),
    path('base', views.base, name='home/'),
 #   path('main_base',views.main_base, name='main_base'),
 #   path('main_base_page',views.main_base_page, name='main_base_page'),
    path('post/new', views.post_new, name='post_new'),
]
