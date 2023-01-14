from django.db import models
from django.utils.text import slugify


def carousel_image_directory_path(instance, filename):

    image_order = slugify(instance.carousel_order)

    return f'carousel/brands/slide {image_order}/{filename}'

class CarouselImage(models.Model):

    image = models.ImageField('Imagem:', upload_to=carousel_image_directory_path)
    carousel_order = models.IntegerField('Ordem no carrossel', unique=True)

    def __str__(self) -> str:
        return f"Imagem {self.carousel_order}"

    class Meta:
        verbose_name = 'Img. Car. Marca'
        ordering = ['carousel_order']
