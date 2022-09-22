from django.contrib import admin
from .models import Bicycle, Brand, Photo


class PhotoInline(admin.TabularInline):
    model = Photo

class BicycleAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('bike_model',)}
    inlines= [PhotoInline, ]

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('name',)}


admin.site.register(Bicycle, BicycleAdmin)
admin.site.register(Brand, BrandAdmin)
