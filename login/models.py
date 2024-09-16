from django.db import models

# Create your models here.
class credential(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)
    def __str__(self):
        return f'{self.Username}, {self.Password}'