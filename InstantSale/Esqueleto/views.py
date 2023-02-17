from pickle import TRUE
from tkinter import Variable
from django.shortcuts import redirect, render
from .models import UsuarioPublicacion, direccion, telefono, usuario, publicacionarticulo, articulo, comentario, favorito, SubastarPublicacion
# from .models import usuario, publicacionarticulo, articulo, CrearPublicacion
from django.contrib import messages 
from django.db.models import Q
from .forms import ArticuloForm
import sys
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
import json

# Create your views here.

def home_view(request, Usuario):
    
    persona=usuario.objects.get(Usuario=Usuario)

    return render(request, "PerfilVacio.html", {"persona":persona})
    

def login(request):
    if request.method=='POST':
        try:
            detalleUsuario=usuario.objects.get(Usuario=request.POST['usuario'], Clave=request.POST['clave'])
            request.session['usuario']=detalleUsuario.Usuario
            # Variable='Andres'
            # return render(request, "Principal.html", {})
            # return redirect('/home/', Variable)
            return redirect('/home/')
        except usuario.DoesNotExist as e:
            messages.success(request, 'Usuario o Contraseña no son correctos.')
    return render(request, "login.html", {})

def CerrarSesion(request):
    try:
        del request.session['usuario']
    except:
        # return render(request, "login.html", {})
        return redirect('/login')
    # return render(request, "login.html", {})
    return redirect('/login')

def contact_view(request):
    return render(request, "contact.html", {})

def about(request):
    return render(request, "about.html", {})

def Bienvenida(request):
    return render(request, "Bienvenida.html", {})

def BarraNavegacion(request):
    listausuarios = usuario.objects.all()
    return render(request, "BarraNavegacion.html", {"usuarios": listausuarios})

# def BarraNavegacion(request):
#     return render(request, "Bienvenida.html", {})

def Usuarios(request):
    busqueda= request.GET.get("Buscar")
    listausuarios = usuario.objects.all()

    if busqueda:
        listausuarios= usuario.objects.filter(
            Q(Usuario__icontains=busqueda) | Q(Email__icontains=busqueda)
        ).distinct()

    return render(request, "ListaUsuarios.html", {"usuarios": listausuarios})

def PerfilPropio(request,Usuario=None):
    if usuario.objects.filter(Usuario=Usuario).exists():
        persona=usuario.objects.get(Usuario=Usuario)
        publicacion=persona.Publicaciones.all()

        if direccion.objects.filter(Usuario_id=persona.id).exists() and telefono.objects.filter(Usuario_id=persona.id).exists():
            Direccion=direccion.objects.get(Usuario_id=persona.id)
            Telefono=telefono.objects.get(Usuario_id=persona.id)

            return render(request,"PerfilPropio.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion), "Direccion":Direccion,"Telefono":Telefono})


        if direccion.objects.filter(Usuario_id=persona.id).exists():
            Direccion=direccion.objects.get(Usuario_id=persona.id)

            return render(request,"PerfilPropio.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion), "Direccion":Direccion})

        if telefono.objects.filter(Usuario_id=persona.id).exists():
            Telefono=telefono.objects.get(Usuario_id=persona.id)

            return render(request,"PerfilPropio.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion), "Telefono":Telefono})
        # try:
        #     persona=usuario.objects.get(Usuario=Usuario)
        #     publicacion=persona.Publicaciones.all()
        #     Direccion=direccion.objects.get(Usuario_id=persona.id)
        #     Telefono=telefono.objects.get(Usuario_id=persona.id)
        # except:
        #     return render(request,"PerfilPropio.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion)})
    return render(request,"PerfilPropio.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion)})

def Perfil(request,id):
    if usuario.objects.filter(id=id).exists():
        persona=usuario.objects.get(id=id)
        publicacion=persona.Publicaciones.all()

        if direccion.objects.filter(Usuario_id=persona.id).exists() and telefono.objects.filter(Usuario_id=persona.id).exists():
            Direccion=direccion.objects.get(Usuario_id=persona.id)
            Telefono=telefono.objects.get(Usuario_id=persona.id)

            return render(request,"PerfilUsuario.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion), "Direccion":Direccion,"Telefono":Telefono})


        if direccion.objects.filter(Usuario_id=persona.id).exists():
            Direccion=direccion.objects.get(Usuario_id=persona.id)

            return render(request,"PerfilUsuario.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion), "Direccion":Direccion})

        if telefono.objects.filter(Usuario_id=persona.id).exists():
            Telefono=telefono.objects.get(Usuario_id=persona.id)

            return render(request,"PerfilUsuario.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion), "Telefono":Telefono})
        # try:
        #     persona=usuario.objects.get(Usuario=Usuario)
        #     publicacion=persona.Publicaciones.all()
        #     Direccion=direccion.objects.get(Usuario_id=persona.id)
        #     Telefono=telefono.objects.get(Usuario_id=persona.id)
        # except:
        #     return render(request,"PerfilPropio.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion)})
    return render(request,"PerfilUsuario.html",{"persona":persona, "publicacion":publicacion, "Tamano":len(publicacion)})

def Principal(request):
    busqueda= request.GET.get("buscar")
    listaPublicaciones = publicacionarticulo.objects.all()
    # listaArticulos = articulo.objects.all()

    if busqueda:
        listaPublicaciones= publicacionarticulo.objects.filter(
            Q(Titulo__icontains=busqueda) | Q(Descripcion__icontains=busqueda) 
            # Q(DineroInicial__icontains=busqueda) |
            # Q(Articulo__icontains =busqueda)
        ).distinct()


    # return render(request, "Principal.html", {"publicaciones": listaPublicaciones,"articulos": listaArticulos})
    return render(request, "Principal.html", {"publicaciones": listaPublicaciones})

def RegistroU(request):
    return render(request, "Registro.html", {})

def RegistrarUsuario(request):
    
    Nombre= request.POST['txtNombre']
    ApellidoPaterno= request.POST['txtApellidoPaterno']
    ApellidoMaterno= request.POST['txtApellidoMaterno']
    Email= request.POST['txtEmail']
    FechaNacimiento= request.POST['txtFechaNacimiento']
    Usuario= request.POST['txtUsuario']
    Clave= request.POST['txtClave']
    ImgPerfil= request.FILES.get('txtImgPerfil')

    usuarios = usuario.objects.create(
        Nombre=Nombre, ApellidoPaterno=ApellidoPaterno, ApellidoMaterno=ApellidoMaterno, 
        Email=Email, FechaNacimiento=FechaNacimiento, Usuario=Usuario, Clave=Clave, ImgPerfil=ImgPerfil
    ) 
    return redirect('/login')

def EditarPerfil(request, id):
    Usuario = usuario.objects.get(id=id)

    return render(request, "EditarPerfil.html", { "usuario":Usuario })

def EdicionPerfil(request,id):
    Nombre= request.POST['txtNombre']
    ApellidoPaterno= request.POST['txtApellidoPaterno']
    ApellidoMaterno= request.POST['txtApellidoMaterno']
    Email= request.POST['txtEmail']
    FechaNacimiento= request.POST['txtFechaNacimiento']
    Usuario= request.POST['txtUsuario']
    Clave= request.POST['txtClave']
    # ImgPerfil= request.FILES.get('txtImgPerfil')

    Persona = usuario.objects.get(id=id)
    Persona.Nombre = Nombre
    Persona.ApellidoPaterno = ApellidoPaterno
    Persona.ApellidoMaterno = ApellidoMaterno
    Persona.Email = Email
    Persona.FechaNacimiento = FechaNacimiento
    Persona.Usuario = Usuario
    Persona.Clave = Clave
    Persona.ImgPerfil = request.FILES.get('txtImgPerfil')

    Persona.save()

    return redirect('/CerrarSesion/')

def ActualizarDirecciones(request, id):
    try:
        Direccion = direccion.objects.get(Usuario_id=id)
    except:
        return render(request, "ActualizarDirecciones.html", { "IdUsuario":id})    
    return render(request, "ActualizarDirecciones.html", { "IdUsuario":id, "Direccion":Direccion})

def ActualizacionDireccion(request,id):
    CallePrincipal= request.POST['txtCallePrincipal']
    CalleSecundaria= request.POST['txtCalleSecundaria']
    Provincia= request.POST['txtProvincia']
    Ciudad= request.POST['txtCiudad']
    Pais= request.POST['txtPais']

    if direccion.objects.filter(Usuario_id=id).exists():
        Direccion = direccion.objects.get(Usuario_id=id)
        Direccion.CallePrincipal = CallePrincipal
        Direccion.CalleSecundaria = CalleSecundaria
        Direccion.Provincia = Provincia
        Direccion.Ciudad = Ciudad
        Direccion.Pais = Pais
        
        Direccion.save()
        # return redirect('/PerfilPropio/'+id)
        return redirect('/home/')
    else:
        direcciones = direccion.objects.create(
            Usuario_id=id, CallePrincipal=CallePrincipal, CalleSecundaria=CalleSecundaria, Provincia=Provincia, 
            Ciudad=Ciudad, Pais=Pais
        )

    # return redirect('/PerfilPropio/'+id)
    return redirect('/home/')

def ActualizarTelefonos(request, id):
    try:
        Telefono = telefono.objects.get(Usuario_id=id)
    except:
        return render(request, "ActualizarTelefonos.html", { "IdUsuario":id})    
    return render(request, "ActualizarTelefonos.html", { "IdUsuario":id, "Telefono":Telefono})

def ActualizacionTelefono(request,id):
    Telefono1= request.POST['txtTelefono1']
    Telefono2= request.POST['txtTelefono2']
    Celular= request.POST['txtCelular']

    if telefono.objects.filter(Usuario_id=id).exists():
        Telefono = telefono.objects.get(Usuario_id=id)
        Telefono.Telefono1 = Telefono1
        Telefono.Telefono2 = Telefono2
        Telefono.Celular = Celular
        
        Telefono.save()
        return redirect('/home/')
    else:
        telefonos = telefono.objects.create(
            Usuario_id=id, Telefono1=Telefono1, Telefono2=Telefono2, Celular=Celular
        )
    return redirect('/home/')

def EliminarUsuario(request, id):
    Usuario = usuario.objects.get(id=id)
    Usuario.delete()

    return redirect('/CerrarSesion/')

def EliminarPublicacion(request, id):
    Publicacion = publicacionarticulo.objects.get(Articulo_id=id)
    Publicacion.delete()

    return redirect('/home/')

def RegistrarArticulo(request, Usuario):
    persona=usuario.objects.get(Usuario=Usuario)
    Formulario=ArticuloForm()
    # if request.method == "POST":
        
    #     form = ArticuloForm(request.POST) 
    #     if form.is_valid():
    #         Producto=articulo()
    #         Producto.Nombre = form.cleaned_data['Nombre']
    #         Producto.Descripcion = form.cleaned_data['Descripcion']
    #         Producto.EstadoProducto = form.cleaned_data['EstadoProducto']
    #         Producto.Categoria = form.cleaned_data['Categoria']
    #         Producto.PaisOrigen = form.cleaned_data['PaisOrigen']
    #         Producto.Color = form.cleaned_data['Color']
    #         Producto.ImgArticulo = request.FILES.get(form.cleaned_data['ImgArticulo'])
    #         Producto.save()
            
    #         # ImgPerfil= request.FILES.get('txtImgPerfil')
    #     else:
    #         print("Error al guardar un Articulo")

    return render(request, "RegistrarArticulo.html", {"PersonaId":persona.id, "FomularioArticulo":Formulario})

def RegistrarPublicacion(request, id):

    if request.method == "POST":
        
        form = ArticuloForm(request.POST) 
        if form.is_valid():
            Producto=articulo()
            Producto.Nombre = form.cleaned_data['Nombre']
            Producto.Descripcion = form.cleaned_data['Descripcion']
            Producto.EstadoProducto = form.cleaned_data['EstadoProducto']
            Producto.Categoria = form.cleaned_data['Categoria']
            Producto.PaisOrigen = form.cleaned_data['PaisOrigen']
            Producto.Color = form.cleaned_data['Color']
            # Producto.ImgArticulo = request.FILES.get(form.cleaned_data['ImgArticulo'])
            # Producto.ImgArticulo = form.cleaned_data['ImgArticulo']
            Producto.ImgArticulo = request.FILES.get('ImgArti')
            Producto.save()
            
        else:
            print("Error al guardar un Articulo")

    return render(request, "RegistrarPublicacion.html", {"IdUsuario":id, "IdProducto":Producto.id})

def HacerPublicacion(request, id):
    NuevaP= publicacionarticulo()

    NuevaP.Articulo_id = request.POST['txtIdArticulo']
    NuevaP.Titulo = request.POST['txtTitulo']
    NuevaP.Descripcion = request.POST['txtDescripcion']
    NuevaP.DineroInicial = request.POST['txtDineroInicial']
    NuevaP.Stock = request.POST['txtStock']
    NuevaP.EstadoPublicacion = True
    NuevaP.FechaHoraSubida = datetime.now()

    NuevaP.FechaHoraRetirada= request.POST['txtFechaRetirada']
    NuevaP.save()
    # FechaRetirada= request.POST['txtFechaRetirada']
    # HoraMinutoRetirada= request.POST['txtHora']

    # Articulo_id= request.POST['txtIdArticulo']
    # Titulo= request.POST['txtTitulo']
    # Descripcion= request.POST['txtDescripcion']
    # DineroInicial= request.POST['txtDineroInicial']
    # Stock= request.POST['txtStock']
    # FechaRetirada= request.POST['txtFechaRetirada']
    # HoraMinutoRetirada= request.POST['txtHora']
    # EstadoPublicacion = True
    # FechaHoraSubida= datetime.now()



    # Fecha1=FechaRetirada.strftime("%Y-%m-%d")
    # Fecha2=HoraMinutoRetirada.strftime("%H:%S:%M")
    # print("Esta es la fecha ahora :c")
    # print(Fecha1+Fecha2)

    # Hola= FechaHoraSubida+""+FechaRetirada


    # NuevaPublicacion = publicacionarticulo.objects.create(
    #     Articulo_id=Articulo_id, Titulo=Titulo, Descripcion=Descripcion, DineroInicial=DineroInicial,
    #     Stock=Stock, EstadoPublicacion=EstadoPublicacion, FechaHoraSubida=FechaHoraSubida, 
    #     FechaHoraRetirada=datetime.now()
    # )

    HolaMundo= UsuarioPublicacion()
    HolaMundo.PublicacionArticulo_id= NuevaP.Articulo_id
    HolaMundo.Usuario_id=id
    HolaMundo.save()
    # NuevaRelacionUsuarioPublicacion=UsuarioPublicacion.objects.create(
    #     PublicacionArticulo_id=NuevaP.id, Usuario_id=id
    # )
    
    return redirect('/home/')

def Subastar(request,id):
    Article=publicacionarticulo.objects.get(Articulo_id=id)
    Persona=UsuarioPublicacion.objects.get(PublicacionArticulo_id=id)
    # ListaComentario= comentario.objects.all()
    if request.method == "POST":
        Comentario=comentario()
        Comentario.PublicacionArticulo_id = id
        Comentario.Comentario = request.POST['txtComentario']
        Comentario.FechaHora = datetime.now()
        Comentario.save()
    ListaComentario= comentario.objects.filter(PublicacionArticulo_id=id)

    return render(request, "PaginaSubastar.html", {"Persona":Persona, "Article":Article, "Comentario":ListaComentario})

def RealizarSubasta(request, id):
    Variable= request.POST['txtUsuario']
    persona=usuario.objects.get(Usuario=Variable)
    Subastar= SubastarPublicacion()

    Subastar.PublicacionArticulo_id= id
    Subastar.Usuario_id= persona.id
    Subastar.Cantidad= request.POST['txtCantidad']
    Subastar.FechaHora= datetime.now()
    Subastar.Estado= True
    
    Subastar.save()

    return redirect('/home/')

def Favoritos(request,id):
    Favorito=favorito()
    Favorito.PublicacionArticulo_id = id
    Favorito.Activo = True
    Favorito.FechaHora = datetime.now()
    Favorito.save()

    return redirect('/home/')

class ComentariosView(View):
    # Para que no me salte el error de csrf
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
        if (id > 0):
            Comentarios= list(comentario.objects.filter(id=id).values())
            if len(Comentarios) > 0:
                Comentario = Comentarios[0]
                datos={'message':"Success",'Comentarios':Comentario}
            else:
                datos={'message':"Tenemos un problema con la muestra de los Comentarios..."}
            return JsonResponse(datos)
        else:
            Comentarios= list(comentario.objects.values())
            if len(Comentarios)>0:
                datos={'message':"Success",'Comentarios':Comentarios}
            else:
                datos={'message':"Tenemos un problema con la muestra de los Comentarios..."}
            return JsonResponse(datos)

    def post(self,request):
        jd= json.loads(request.body)
        print(jd)
        comentario.objects.create(PublicacionArticulo_id=jd['PublicacionArticulo_id'], Comentario=jd['Comentario'], FechaHora=jd['FechaHora'])
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id):
        jd= json.loads(request.body)
        Comentarios= list(comentario.objects.filter(id=id).values())
        if len(Comentarios) > 0:
            Comentario= comentario.objects.get(id=id)
            Comentario.PublicacionArticulo_id=jd['PublicacionArticulo_id']
            Comentario.Comentario=jd['Comentario']
            Comentario.FechaHora=jd['FechaHora']
            Comentario.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Tenemos un problema con la edicion del comentario..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        Cometarios= list(comentario.objects.filter(id=id).values())
        if len(Cometarios) > 0:
            comentario.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else:
            datos={'message':"Tenemos un problema con la eliminacion del comentario..."}
        return JsonResponse(datos)

class SubastaView(View):
    # Para que no me salte el error de csrf
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
        if (id > 0):
            Subastas= list(SubastarPublicacion.objects.filter(id=id).values())
            if len(Subastas) > 0:
                Subastar = Subastas[0]
                datos={'message':"Success",'Subastar':Subastar}
            else:
                datos={'message':"Tenemos un problema con la muestra de las Subastas..."}
            return JsonResponse(datos)
        else:
            Subastas= list(SubastarPublicacion.objects.values())
            if len(Subastas)>0:
                datos={'message':"Success",'Subastas':Subastas}
            else:
                datos={'message':"Tenemos un problema con la muestra de las Subastas..."}
            return JsonResponse(datos)

    def post(self,request):
        jd= json.loads(request.body)
        print(jd)
        SubastarPublicacion.objects.create(PublicacionArticulo_id=jd['PublicacionArticulo_id'], Usuario_id=jd['Usuario_id'], Cantidad=jd['Cantidad'], FechaHora=jd['FechaHora'], Estado=jd['Estado'])
        datos={'message':"Success"}
        return JsonResponse(datos)
        

    def put(self,request,id):
        jd= json.loads(request.body)
        Subastas= list(SubastarPublicacion.objects.filter(id=id).values())
        if len(Subastas) > 0:
            Subastar= SubastarPublicacion.objects.get(id=id)
            Subastar.PublicacionArticulo_id=jd['PublicacionArticulo_id']
            Subastar.Usuario_id=jd['Usuario_id']
            Subastar.Cantidad=jd['Cantidad']
            Subastar.FechaHora=jd['FechaHora']
            Subastar.Estado=jd['Estado']
            
            Subastar.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Tenemos un problema con la edicion de la Subasta..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        Subastas= list(comentario.objects.filter(id=id).values())
        if len(Subastas) > 0:
            SubastarPublicacion.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else:
            datos={'message':"Tenemos un problema con la eliminacion de la Subasta..."}
        return JsonResponse(datos)