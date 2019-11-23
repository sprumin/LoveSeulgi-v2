from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from fanpage.models import Photos
from fanpage.utility import get_photos


# Create your views here.
class PhotoView(View):
    def get(self, request, photo_id=None):
        """ Photo List, Photo Info """
        if photo_id:
            try:
                result = Photos.objects.get(idx=photo_id)
                status = 200
            except Exception as e:
                print(e)
                result = {"Error": "Invalid photo id"}
                status = 400 
        else:
            width = request.GET.get("width", None)
            height = request.GET.get("height", None)
            max_width = request.GET.get("max_width", None)
            max_height = request.GET.get("max_height", None)

            result = get_photos(width, height, max_width, max_height)
            status = 200
        
        return JsonResponse(result, status=status)

    def put(self, request, photo_id):
        """ Photo Info Update """
        pass

    def delete(self, request, photo_id):
        """ Photo Delete """
        pass