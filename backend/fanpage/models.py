from django.db import models

import uuid


# Create your models here.
class Album(models.Model):
    # Save image from crawler
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to="CrawlImage")
    photo_name = models.CharField(default=uuid.uuid4(), max_length=256)
    photo_link = models.CharField(default="", max_length=2048)
    photo_source = models.CharField(default="", max_length=2048)
    view = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
