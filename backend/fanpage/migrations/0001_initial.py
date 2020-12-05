# Generated by Django 3.1.4 on 2020-12-05 10:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='CrawlImage')),
                ('photo_name', models.CharField(default=uuid.UUID('2a7ed827-7982-45d1-b21b-eddb7cd1adaf'), max_length=256)),
                ('photo_link', models.CharField(default='', max_length=2048)),
                ('photo_source', models.CharField(default='', max_length=2048)),
                ('view', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]