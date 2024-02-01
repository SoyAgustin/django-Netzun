from django.db import models

class Cathegory(models.Model):
    name = models.CharField(max_length=255)

    #Sobrecarga del método string para cuando aparezca en consola
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255) #cadena de caracteres de hasta 255 cartacteres
    description = models.TextField() #texto de longitud ilimitada
    price = models.IntegerField() #entero
    cathegory = models.ForeignKey(Cathegory,on_delete = models.CASCADE,related_name="products") 
    is_active = models.BooleanField(default = True)
    #CASCADE hace que cuando eliminamos una categoría no se elimina todo el producto
    #related_name se usa para usarlo en el shell cuando se usan filtros, por ej. cathegory.products.all()


    def __str__(self):
        return self.name
    
    #Con esto se puede llamar al nombre como propiedad (método estático sin instanciar la clase) 
    #por ej product.cathegory_name (tal que product es un producto)
    @property
    def cathegory_name(self):
        return self.cathegory.name