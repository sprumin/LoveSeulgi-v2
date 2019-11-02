from django.db import models


# Create your models here.
class Photos(models.Model):
    idx = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to="image", unique=True)
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=2048)
    source = models.CharField(max_length=2048)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_gif = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Photo"
    
    def __str__(self):
        return self.title


class InvalidPage(models.Model):
    idx = models.AutoField(primary_key=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    content = models.TextField(max_length=2048, blank=True, null=True)

    class Meta:
        verbose_name = "Invalid Page"
