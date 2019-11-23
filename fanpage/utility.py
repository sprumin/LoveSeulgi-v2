from fanpage.models import Photos


def get_photos(width, height):
    """ return photos gte width, height"""
    max_width = width + 100
    max_height = height + 100
    return Photos.objects.filter(
        width__gte=width, width__lte=max_width,
        height__gte=height, height__lte=max_height
    )