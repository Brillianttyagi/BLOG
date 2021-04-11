from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    body = models.TextField(max_length=100000)
    created = models.DateField(
        auto_now_add=True
    )
    image = models.ImageField(upload_to = 'pics')
    author = models.CharField(max_length=60)
    read_time = models.CharField(max_length=10)
