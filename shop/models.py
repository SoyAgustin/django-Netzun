from django.db import models

class Cathegory(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255) #cadena de caracteres de hasta 255 cartacteres
    description = models.TextField() #texto de longitud ilimitada
    price = models.IntegerField() #entero
    cathegory = models.ForeignKey(Cathegory,on_delete = models.CASCADE) #CASCADE hace que cuando eliminamos una categoría no se elimina todo el producto
