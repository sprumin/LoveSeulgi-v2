from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class UserView(View):
    def get(self, request, user_id=None):
        """ User List, User Info """
        pass
    def post(self, request):
        """ User Register """
        pass
    def put(self, request, user_id):
        """ User Info Update """
        pass
    def delete(self, request, user_id):
        """ User Delete """
        pass