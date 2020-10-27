from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=64, null=True)
    path = models.FileField(upload_to='files')
    unique = models.CharField(max_length=256)
