from django.db import models

# Create your models here.
class cuenta(models.Model):
 nombre = models.CharField(max_length=200)
 clave = models.CharField(max_length=200)
 numero = models.CharField(max_length=20)
