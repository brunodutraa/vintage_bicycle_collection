from django.db import models
from django.utils.text import slugify

from collection.utils import make_thumbnail

from .bicycle import Bicycle


def bicycle_photo_directory(instance, filename):
    bicycle_model = slugify(instance.bicycle.bike_model)
    return f'bicycles/{bicycle_model}/original_photos/{filename}'


def bicycle_small_photo_directory(instance, filename):
    bicycle_model = slugify(instance.bicycle.bike_model)
    return f'bicycles/{bicycle_model}/small_photos/{filename}'


class Photo(models.Model):
    """This class defines a photo of a bicycle"""

    bicycle = models.ForeignKey(
        Bicycle, on_delete=models.CASCADE, verbose_name='Bicicleta')
    photo = models.ImageField('Foto', upload_to=bicycle_photo_directory)
    small_photo = models.ImageField(editable=False, upload_to=bicycle_small_photo_directory)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos',

    def save(self, *args, **kwargs):
        self.small_photo = make_thumbnail(self.photo)
        super().save(*args, **kwargs)
