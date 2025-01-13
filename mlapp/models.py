from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=200)
    phone=models.PositiveIntegerField()
    def __str__(self):
        return f"{self.name}"