from django.contrib import admin
from django.utils.safestring import mark_safe

from fanpage.models import Photos, InvalidPage


class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ("image_viewer", )

    def image_viewer(self, obj):
        return mark_safe(
            "<a href='{}'><img src='{}' width='{}' height='{}' /></a>".format(
                obj.photo.url, obj.photo.url, obj.photo.width / 3, obj.photo.height / 3))

    image_viewer.short_description = 'Image Viewer'

# Register your models here.
admin.site.register(Photos, PhotoAdmin)
admin.site.register(InvalidPage)