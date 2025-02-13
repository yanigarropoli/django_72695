from django.db import models

# Create your models here

class Auto (models.Model):
    modelo= models.CharField(max_length=20)
    marca= models.CharField(max_length=20)
    descripcion= models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f" {self.modelo} {self.marca}"

