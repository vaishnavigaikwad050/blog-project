from django.db import models

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=100000000)
    dat = models.DateTimeField(auto_now_add=True)
    upd = models.DateTimeField(auto_now=True)


