from django.shortcuts import render

from fanpage.models import Photos


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        "photos": Photos.objects.all(),
    })