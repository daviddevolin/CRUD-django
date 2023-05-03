from django.db import models

# Create your models here.

#criando model user
class User (models.Model):
    nome = models.CharField(max_length=100)

#tratando a froma como é exibido o user 
    def __str__(self):
        return self.nome