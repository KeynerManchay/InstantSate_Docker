from distutils.command.upload import upload
from email.policy import default
from django.db import models


# Create your models here.

Articulo_Estado = [
    (1, 'Nuevo'),
    (2, 'Usado')
]

Articulo_Categoria = [
    (1, 'Clasico'),
    (2, 'Retro'),
    (3, 'Ropa'),
    (4, 'Deportivo'),
    (5, 'Electronicos'),
    (6, 'Tecnologia'),
    (7, 'Arte'),
    (8, 'Salud'),
    (9, 'Entretenimiento'),
    (10, 'Software'),
    (11, 'Automotriz'),
    (12, 'Otro')
]

Articulo_PaisOrigen = [
    (1, 'Ecuador'),
    (2, 'EEUU'),
    (3, 'Peru'),
    (4, 'Colombia'),
    (5, 'Venezuela'),
    (6, 'Brasil'),
    (7, 'Uruguay'),
    (8, 'Chile'),
    (9, 'Bolivia'),
    (10, 'Paraguay'),
    (11, 'Otro')
]

Articulo_Color = [
    (1, 'Amarillo'),
    (2, 'Azul'),
    (3, 'Rojo'),
    (4, 'Naranja'),
    (5, 'Verde'),
    (6, 'Morado'),
    (7, 'Rosado'),
    (8, 'Negro'),
    (9, 'Gris'),
    (10, 'Cafe'),
    (11, 'Blanco'),
    (12, 'Otro')
]

class articulo(models.Model):
    Nombre= models.CharField(max_length=120, null=False, blank=False)
    Descripcion= models.CharField(max_length=200, null=False, blank=False)
    EstadoProducto= models.IntegerField(null=False, blank=False, choices=Articulo_Estado, default=1)  
    Categoria= models.IntegerField(null=False, blank=False, choices=Articulo_Categoria, default=1 )
    PaisOrigen= models.IntegerField(null=False, blank=False, choices=Articulo_PaisOrigen, default=1)
    Color= models.IntegerField(null=True, blank=False, choices=Articulo_Color)
    ImgArticulo= models.ImageField(upload_to="Articulos", default='Articulos/Nada.jpg',null=True)

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.Nombre, self.Descripcion, self.EstadoProducto, self.Categoria, self.PaisOrigen, self.Color)

class publicacionarticulo(models.Model):
    Articulo= models.OneToOneField(articulo, on_delete=models.CASCADE, primary_key=True,)
    # Usuario= models.ManyToManyField(usuario)
    Titulo= models.CharField(max_length=120, null=False, blank=False)
    Descripcion= models.CharField(max_length=120, null=False, blank=False)
    DineroInicial= models.FloatField(default=0.00)
    Stock= models.IntegerField()
    EstadoPublicacion= models.BooleanField()
    FechaHoraSubida= models.DateTimeField()
    FechaHoraRetirada= models.DateTimeField()

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6}".format(self.Articulo, self.Titulo, self.Descripcion, self.Stock, self.EstadoPublicacion, self.FechaHoraSubida, self.FechaHoraRetirada)


class comentario(models.Model):
    PublicacionArticulo= models.ForeignKey(publicacionarticulo, null=False, blank=False, on_delete=models.CASCADE)
    Comentario= models.CharField(max_length=350, null=False, blank=False)
    FechaHora= models.DateTimeField()
  
    def __str__(self):
        return "{0},{1},{2}".format(self.PublicacionArticulo, self.Comentario, self.FechaHora)

class favorito(models.Model):
    PublicacionArticulo= models.ForeignKey(publicacionarticulo, null=False, blank=False, on_delete=models.CASCADE)
    Activo= models.BooleanField()
    FechaHora= models.DateTimeField()
  
    def __str__(self):
        return "{0},{1},{2}".format(self.PublicacionArticulo, self.Activo, self.FechaHora)

class usuario(models.Model):
    Nombre= models.CharField(max_length=45, null=False, blank=False) 
    ApellidoPaterno= models.CharField(max_length=45, null=False, blank=False)
    ApellidoMaterno= models.CharField(max_length=45, null=False, blank=False)
    Email= models.EmailField(max_length=350, null=False, blank=False)
    FechaNacimiento= models.DateField()
    Usuario= models.CharField(max_length=35, null=False, blank=False)
    Clave= models.CharField(max_length=45, null=False, blank=False)
    ImgPerfil= models.ImageField(upload_to="PerfilUsuarios", default='PerfilUsuarios/PerfilDefaulth.jpg',null=True)
    # Vende= models.ManyToManyField(usuario)
    Publicaciones= models.ManyToManyField(publicacionarticulo, through='UsuarioPublicacion')
    Subasta= models.ManyToManyField(publicacionarticulo, related_name = 'EntrarSubasta',through='SubastarPublicacion')
    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7}".format(self.Nombre, self.ApellidoPaterno, self.ApellidoMaterno, self.Email, self.FechaNacimiento, self.Usuario, self.Clave, self.Publicaciones)

class SubastarPublicacion(models.Model):
    PublicacionArticulo= models.ForeignKey(publicacionarticulo, related_name = 'Publicaciones',on_delete=models.CASCADE, null=True)
    Usuario= models.ForeignKey(usuario,on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    FechaHora= models.DateTimeField()
    Estado= models.BooleanField()

    def __str__(self):
        return "{0},{1},{2},{3},{4}".format(self.PublicacionArticulo, self.Usuario,self.Cantidad, self.FechaHora, self.Estado)

class UsuarioPublicacion(models.Model):
    PublicacionArticulo= models.ForeignKey(publicacionarticulo, on_delete=models.CASCADE, null=True)
    Usuario= models.ForeignKey(usuario, on_delete=models.CASCADE)
    def __str__(self):
        return "{0},{1}".format(self.PublicacionArticulo, self.Usuario)

class vender(models.Model):
    Vendedor= models.ForeignKey(usuario, null=False, related_name = 'Vendedor',blank=False, on_delete=models.CASCADE)
    Cliente= models.ForeignKey(usuario, null=False, related_name = 'Cliente', blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return "{0},{1}".format(self.Vendedor, self.Cliente)

class telefono(models.Model):
    Usuario = models.OneToOneField(usuario, related_name = 'Propietario', on_delete=models.CASCADE, primary_key=True,)
    Telefono1= models.CharField(max_length=10, null=False, blank=False) 
    Telefono2= models.CharField(max_length=10, null=True)
    Celular= models.CharField(max_length=10, null=False, blank=False)
    def __str__(self):
        return "{0},{1},{2},{3}".format(self.Usuario, self.Telefono1, self.Telefono2, self.Celular)

class direccion(models.Model):
    Usuario = models.OneToOneField(usuario, related_name = 'PersonaDireccion', on_delete=models.CASCADE, primary_key=True,)
    CallePrincipal= models.CharField(max_length=120, null=False, blank=False) 
    CalleSecundaria= models.CharField(max_length=120, null=True)
    Provincia= models.CharField(max_length=50, null=False, blank=False)
    Ciudad= models.CharField(max_length=50, null=False, blank=False)
    Pais= models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.Usuario, self.CallePrincipal, self.CalleSecundaria, self.Provincia, self.Ciudad, self.Pais)

