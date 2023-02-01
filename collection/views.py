from multiprocessing import context

import plotly.express as px
from django.shortcuts import get_object_or_404, render
from plotly.offline import plot

from core.models import CarouselImage

from .models import Bicycle, Brand


def all_brands(request):
    brand_list = []
    carousel_list = []

    bbrand_query = Brand.objects.all()
    carousel_query = CarouselImage.objects.all()
    for brd in bbrand_query:
        brand_list.append(brd)
    for car in carousel_query:
        carousel_list.append(car)
    context = {
        'brand_query': brand_list,
        'carousel_query': carousel_list
    }

    return render(request, 'collection/brand.html', context)


def brand_detail(request, slug):

    bike_query = None

    try:
        brand = get_object_or_404(Brand, slug=slug)
    except:
        brand = False

    if brand:
        bike_query = brand.bicycle_set.all()

    context = {
        'brand_obj': brand,
        'bike_query': bike_query,
        'brand_slug': slug,
    }

    return render(request, 'collection/brand_detail.html', context)


def bike_detail(request, bikeslug, brandslug=None):

    bike_photo_query = None

    try:
        bike = get_object_or_404(Bicycle, slug=bikeslug)
    except:
        bike = False

    if bike:
        bike_photo_query = bike.photo_set.all()

    context = {
        'bikeslug': bikeslug,
        'bike': bike,
        'bike_photos': bike_photo_query,
    }

    return render(request, 'collection/bike_detail.html', context)

def slider_mobile(request):
    return render(request, 'collection/slider.html')