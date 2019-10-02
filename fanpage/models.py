from django.db import models


# Create your models here.
class Photos(models.Model):
    idx = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to="image", unique=True)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=2048)
    source = models.CharField(max_length=2048)
    size = models.CharField(max_length=16)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_gif = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Trashcan(models.Model):
    idx = models.AutoField(primary_key=True)
    link = models.CharField(max_length=2048)