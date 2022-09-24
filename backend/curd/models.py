from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=123,null=False)
    # age = models.IntegerField(null=False)

