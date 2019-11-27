from fanpage.models import Photos


def get_photos(width=None, height=None, max_width=None, max_height=None):
    """ return photos gte width, height"""
    photos = Photos.objects.all()
    
    if width:
        photos = photos.filter(width__gte=width)
    if height:
        photos = photos.filter(height__gte=height)
    if max_width:
        photos = photos.filter(width__lte=max_width)
    if max_height:
        photos = photos.filter(height__lte=max_height)
    
    return photos
