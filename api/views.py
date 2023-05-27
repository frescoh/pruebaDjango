import django.db
from django.shortcuts import render,get_object_or_404

# Agregados
from django.http import JsonResponse
from producto_app.models import Producto
from django.forms.models import model_to_dict

def listado_productos(request):
    productos= list(Producto.objects.values())
    return  JsonResponse(productos,safe=False)

def detalle_producto(request,producto_id):
    producto= get_object_or_404(Producto,id=producto_id)
    producto_dict= model_to_dict(producto)
    return JsonResponse(producto_dict,safe=False)