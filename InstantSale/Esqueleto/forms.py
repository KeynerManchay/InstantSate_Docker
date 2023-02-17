from django import forms
from .models import articulo

# class RegistroAsignatura(forms.ModelForm):
#     class Meta:
#         model = asignatura
#         fields=["Materia", "Profesor","HorasSemana","VecesSemana"]


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = articulo
        # fields="__all__"
        # ["Nombre", "Descripcion","EstadoProducto","Categoria","PaisOrigen","Color","ImgArticulo"]
        fields=["Nombre", "Descripcion","EstadoProducto","Categoria","PaisOrigen","Color"]



