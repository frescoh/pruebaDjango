from django.urls import path
from . import views # agregado

urlpatterns = [
    path('',views.index,name='index'), # Se comunica con el view
    path('ejemplo/',views.ejemplo_template,name='ejemplo'),
    path('productos/listado/',views.listado_productos,name='listado_productos'),
    path('productos/nuevo/',views.nuevo_producto,name='nuevo_producto'),
    path('productos/modificar/<int:producto_id>',views.modificar_producto,name='modificar_producto'),
    path('productos/eliminar/<int:producto_id>',views.eliminar_producto,name='eliminar_producto'),
    path('productos/crear_producto',views.ProductoCreateView.as_view(),name='crear_producto'),
    path('productos/desactivar/<int:producto_id>',views.desactivar_producto,name='desactivar_producto'),
    path('productos/activar/<int:producto_id>',views.activar_producto,name='activar_producto'),
]