"""InstantSale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Esqueleto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',contact_view),
    path('about/',about),
    path('home/',Principal),
    path('',Bienvenida),
    path('Usuarios/',Usuarios),
    path('Registro/',RegistroU),
    path('RegistroUsuario/',RegistrarUsuario),
    path('PerfilPropio/EliminarUsuario/<id>', EliminarUsuario),
    path('PerfilPropio/EliminarPublicacion/<id>', EliminarPublicacion),
    path('PerfilPropio/EditarPerfil/<id>', EditarPerfil),
    path('PerfilPropio/EditarPerfil/EdicionPerfil/<id>', EdicionPerfil),
    path('PerfilPropio/ActualizarDirecciones/<id>', ActualizarDirecciones),
    path('PerfilPropio/ActualizarDirecciones/ActualizacionDireccion/<id>', ActualizacionDireccion),
    path('PerfilPropio/ActualizarTelefonos/<id>', ActualizarTelefonos),
    path('PerfilPropio/ActualizarTelefonos/ActualizacionTelefono/<id>', ActualizacionTelefono),
    path('login/',login),
    path('CerrarSesion/',CerrarSesion),
    path('PerfilPropio/<Usuario>',PerfilPropio),
    path('Perfil/<id>',Perfil),
    path('home/RegistrarArticulo/<Usuario>',RegistrarArticulo),
    path('home/RegistrarArticulo/RegistrarPublicacion/<id>',RegistrarPublicacion),
    path('home/RegistrarArticulo/RegistrarPublicacion/HacerPublicacion/<id>',HacerPublicacion),
    path('home/Subastar/<id>',Subastar),
    path('Perfil/Subastar/<id>',Subastar),
    path('home/Favorito/<id>',Favoritos),
    path('home/Subastar/RealizarSubasta/<id>',RealizarSubasta),
    path('Esqueleto/', include('Esqueleto.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)