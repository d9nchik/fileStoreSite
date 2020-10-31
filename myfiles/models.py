from django.db import models
from django.utils.timezone import now

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=64, null=True)
    path = models.FileField(upload_to='files')
    unique = models.CharField(max_length=5)
    date_of_upload = models.DateTimeField(default=now)
