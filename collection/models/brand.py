from multiprocessing import context
from django.db import models
from django.utils.text import slugify
from collection.utils import make_thumbnail


def brand_logo_directory(instance, filename):
    return f"brands/{instance.slug}/logo/{filename}"

class Brand(models.Model):
    """This class defines the attrbute of a bicycle brand"""

    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=500, help_text="Breve descrição da marca (até 500 caracteres). ")
    logo = models.ImageField('Imagem do logotipo', upload_to=brand_logo_directory)
    slug = models.SlugField('Identificador', unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.logo = make_thumbnail(self.logo)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

