from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    created = models.DateTimeField(
        auto_now_add=True
    )
    auther = models.CharField(max_length=60)
    read_time = models.IntegerField()
