from django.db import models

# Create your models here.
class guest(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    messages=models.TextField(500)


    def __str__(self) -> str:
       return self.name
   