from io import BytesIO
from PIL import Image
from django.core.files import File


def make_thumbnail(image, size=(800, 800)):
    """This function make and return a small image with 854 X 480"""

    im = Image.open(image)

    im.convert("RGB")

    im.thumbnail(size)

    thumb_io = BytesIO()

    im.save(thumb_io, 'JPEG')

    thumbnail = File(thumb_io, name=image.name)

    return thumbnail