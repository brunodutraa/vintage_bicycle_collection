from django.urls import path
from collection.views import all_brands, bike_detail, brand_detail, plot_view

urlpatterns = [
    path('marcas/', all_brands, name='brands'),
    path('marcas/<slug:slug>', brand_detail, name = 'brand_detail'),
    path('marcas/<slug:brandslug>/<slug:bike_slug>', bike_detail, name = 'bike_detail'),
    path('', plot_view),
]
