from django.contrib import admin

# Register your models here.

from .models import *


# # # Register your models here.

admin.site.register(usuario)
admin.site.register(telefono)
admin.site.register(direccion)
admin.site.register(vender)
admin.site.register(articulo)
admin.site.register(publicacionarticulo)
admin.site.register(UsuarioPublicacion)
admin.site.register(comentario)
admin.site.register(favorito)
# admin.site.register(subasta)
admin.site.register(SubastarPublicacion)

