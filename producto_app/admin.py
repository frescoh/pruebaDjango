from django.contrib import admin

# Register your models here.
from producto_app.models import Marca, Producto

class ProductoAdmin(admin.ModelAdmin):
    model= Producto
    list_display= 'id','nombre','precio','marca'
    search_fields='marca__nombre',
    list_filter=['marca__nombre']

class MarcaAdmin(admin.ModelAdmin):
    model= Marca
    list_display= 'id','nombre'
    search_fields='nombre',


admin.site.register(Producto,ProductoAdmin)
admin.site.register(Marca,MarcaAdmin)