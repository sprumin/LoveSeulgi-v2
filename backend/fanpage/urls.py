from django.urls import path

from fanpage.views import index

urlpatterns = [
    path("index", index),
]