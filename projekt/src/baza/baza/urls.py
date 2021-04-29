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
# from strony import views
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Start, name='home/'),
    path('StronaGlowna', views.StronaGlowna, name='home_page'),
    path('zakladanie_konta', views.zakladanie_konta, name='home/'),
    path('Statystyki', views.Statystyki, name='statystyki'),
    path('Roczniki', views.Roczniki, name='roczniki'),
    path('Regulamin', views.Regulamin, name='regulamin'),
    path('Projekt', views.Projekt, name='rozwiniecie'),
    path('Omnie', views.Omnie, name='omnie'),
    path('Kontakt', views.Kontakt, name='kontakt'),
    path('rocznik/<int:lata>/', views.rocznik, name='latapodstrony'),
    path('base', views.base, name='home/'),
 #   path('main_base',views.main_base, name='main_base'),
 #   path('main_base_page',views.main_base_page, name='main_base_page'),
    path('post/new', views.post_new, name='post_new'),
]
