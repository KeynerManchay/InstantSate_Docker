from django.urls import path
from .views import ComentariosView, SubastaView

urlpatterns=[
    #Comentarios
    path('comentario/',ComentariosView.as_view(), name='comentarios_list'),
    path('comentario/<int:id>', ComentariosView.as_view(), name='comentarios_process'),

    #Subasta
    path('subastar/',SubastaView.as_view(), name='subastas_list'),
    path('subastar/<int:id>', SubastaView.as_view(), name='subastas_process')
]