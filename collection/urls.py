from django.urls import path

from collection.views import (all_brands, bike_detail, brand_detail,
                              slider_mobile)

urlpatterns = [
    path('marcas/', all_brands, name='brands'),
    path('marcas/<slug:slug>', brand_detail, name='brand_detail'),
    path('marcas/<slug:brandslug>/<slug:bikeslug>',
         bike_detail, name='bike_detail'),
    path('slider', slider_mobile, name='slider-mobile'),
]
