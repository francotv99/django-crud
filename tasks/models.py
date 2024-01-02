from django.db import models


# Create your models here.

#creamos nuetra propia tabla 
class Pais(models.Model):
    #charfiel para texto corto
    codigo=models.IntegerField(max_length=100, blank=True, null=True) 
    #textfiel para texto largo, blank es que por defecto campo vacio
    description=models.CharField(max_length=1000)

    isActive=models.BooleanField(default=True)
    
    #hace que se muetre en el panel con su nombre
    def __str__(self):
        return f"{self.description} - código {str(self.codigo) if self.codigo else 'N/A'}"
    
class Estado(models.Model):
    idpais=models.ForeignKey(Pais,on_delete=models.CASCADE)
    codigo=models.CharField(max_length=100)
    #textfiel para texto largo, blank es que por defecto campo vacio
    description=models.CharField(max_length=1000)
    isActive=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.description} - País: {self.idpais.description}" 