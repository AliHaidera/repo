from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=246)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=246)

    def __str__(self):
        return self.email
