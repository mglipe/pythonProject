from pyexpat import model
from django.db import models

# Create your models here.

class Produto(models.Model):
    name = models.CharField(max_length= 50)
    preco = models.DecimalField(max_digits= 10, decimal_places= 2)


