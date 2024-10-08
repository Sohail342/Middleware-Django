from django.db import models

class RegModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
