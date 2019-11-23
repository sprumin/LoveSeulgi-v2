from django.shortcuts import render

from fanpage.models import Photos
from fanpage.utility import get_photos


# Create your views here.
def index(request):
    """ index page. show full screen slide images """
    template_name = "index.html"

    photo_width = 1900
    photo_height = 1000
    photos = get_photos(photo_width, photo_height)

    return render(request, template_name, {"photos": photos})