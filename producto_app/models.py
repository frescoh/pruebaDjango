from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre= models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.FloatField()
    marca= models.ForeignKey(Marca, 
        related_name='productos',
        on_delete=models.CASCADE,
    )
    activo= models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}   "