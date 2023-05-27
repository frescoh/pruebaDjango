from django.urls import path

from . import views

urlpatterns = [
    path('productos/',views.listado_productos,name='listado_productos'),
    path('productos/<int:producto_id>',views.detalle_producto,name= 'detalle_productos'),
]