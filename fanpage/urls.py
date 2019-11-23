from django.urls import path

from fanpage.views import PhotoView

urlpatterns = [
    path('', PhotoView.as_view()),
    path('<int:photo_id>', PhotoView.as_view()),
]