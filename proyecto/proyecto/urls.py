"""proyecto URL Configuration

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
from django.urls import path,include
from django.conf import settings
from crud.urls import pages_patters
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name="inicio"),
    path('juegos',views.juego,name="juegos"),
    path('juegos/detalle/<int:id>/',views.detalle,name="detalle"),
    path('distribuidor/<int:id>/',views.distribuidora,name="distribuidora"),
    path('genero/detalle/<int:id>/',views.generos,name="genero"),
    path('genero',views.geneross,name="geneross"),
    path('plataforma',views.plataforma,name="plataformas"),
     path('plataforma/<int:id>',views.plataformas,name="plataformasd"),
    path('administrador/', include(pages_patters)),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
