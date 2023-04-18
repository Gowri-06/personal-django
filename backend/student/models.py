from django.db import models
from django.utils import timezone
# Create your models here.

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=123,null=False)
    age = models.IntegerField(null=False)
    roll_no = models.IntegerField(null=False)
    place = models.TextField(null=False)
    email_id = models.EmailField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now) 

    # created_by = models.DateTimeField(default=timezone.now)
    # modified_by = models.DateTimeField(default=timezone.now)


