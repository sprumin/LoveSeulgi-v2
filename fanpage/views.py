from django.core import serializers
from django.http import HttpResponse
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
        
        result = serializers.serialize('json', result)
        
        return HttpResponse(result, content_type="text/json-comment-filtered", status=status)
    
    def post(self, request):
        """ Photo Add """
        res_photo = request.FILES
        # 이거 opencv 써서 이미지 정보 뺴와야댈거가틈
        # 아무리 생각해도 유저가 이미지 정보를 일일히 입력하는것도 이상하고
        # 그렇다고 테이블 따로파자니 어 괜찮은거같기도 고민좀 해봅시다.
        # 굳이 지금 필요한건 아니고 나중에 유저가 이미지 추가하는 기능 생기면 작업하기로
        # 일단은 조회(유저)랑 삭제(어드민)만 필요함

    def put(self, request, photo_id):
        """ Photo Info Update """
        pass

    def delete(self, request, photo_id):
        """ Photo Delete """
        try:
            photo = Photos.objects.get(idx=photo_id)
            photo.delete()

            result = {"result": f"Photo {photo_id} is deleted"}
            status = 200
        except Exception as e:
            print(e)
            result = {"error": "Invalid photo id"}
            status = 400

        return JsonResponse(result, status=status)