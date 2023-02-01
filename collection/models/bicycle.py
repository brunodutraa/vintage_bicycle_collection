from django.db import models
from django.utils.text import slugify

from .brand import Brand


class Bicycle(models.Model):
    """This class defines the attributes of a bicycle"""

    bike_brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, verbose_name='Marca')
    bike_model = models.CharField('Modelo', max_length=100)
    year = models.IntegerField('Ano de fabricação')
    description = models.TextField(
        'Descrição', help_text='Nível de originalidade, história...', max_length=400, blank=True)
    slug = models.SlugField('Identificador', unique=True)

    def __str__(self) -> str:
        return f"{self.bike_brand} - {self.bike_model} - {self.year}"

    class Meta:
        verbose_name = 'Bicicleta'
        verbose_name_plural = 'Bicicletas'
