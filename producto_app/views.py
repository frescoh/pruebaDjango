from django.shortcuts import render,redirect

# Agregados
from django.http import HttpResponse 
from . models import Marca,Producto

# Ver vista basada en clase
# Para vista basada en clase
from django.views.generic import CreateView
from producto_app.forms import ProductoForm


# Create your views here.
def index(request):
    return redirect("/home/productos/listado")

def ejemplo_template(request):
    # context= {
    #     'nombre': 'Hernan',
    #     'apellido': 'Fresco',
    #     'curso': 'Django'
    # }
    marcas= Marca.objects.all()
    return render(request,"producto_app/ejemplo.html",{"marcas":marcas})

def listado_productos(request):
    productos= Producto.objects.all()
    context= {'productos':productos}
    return render(request,"producto_app/listado_productos.html",context)

def nuevo_producto(request):
    context= {'marcas':Marca.objects.all()}
    if request.POST:
        nombre= request.POST['nombre']
        precio= request.POST['precio']
        marca_id= request.POST['marca']
        
        Producto.objects.create(nombre=nombre,precio=precio,marca_id=marca_id)
        print("Producto creado satisfactoramente")
    return render(request,"producto_app/formulario.html",context)

def modificar_producto(request,producto_id):
    marcas= Marca.objects.all()
    producto= Producto.objects.get(id=producto_id)
    context= {
        'marcas': marcas,
        'producto': producto
    }
    if request.POST:
        nombre= request.POST['nombre']
        precio= request.POST['precio']
        marca_id= request.POST['marca']
        
        producto.nombre = nombre
        producto.precio = precio
        producto.marca_id = marca_id
        producto.save()
        
    return render(request,"producto_app/modificar_producto.html",context)

def eliminar_producto(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return HttpResponse(f"El producto con ID {producto_id} fue eliminado")

def desactivar_producto(request,producto_id):
    producto= Producto.objects.get(id=producto_id)
    producto.activo = False
    producto.save()
  
    return redirect('/home/productos/listado')

def activar_producto(request,producto_id):
    producto= Producto.objects.get(id=producto_id)
    producto.activo = True
    producto.save()

    return redirect('/home/productos/listado')



# Vista basada en clase
class ProductoCreateView(CreateView):
    template_name = "producto_app/nuevo_producto.html"
    model= Producto
    form_class = ProductoForm
    success_url = '/home/productos/listado'