from multiprocessing import context

import plotly.express as px
from django.shortcuts import get_object_or_404, render
from plotly.offline import plot

from .models import Bicycle, Brand


def all_brands(request):
    lista = []
    fotos = []
    bbrand_query = Brand.objects.all()

    for brd in bbrand_query:
        # fotos.append(brd.im)
        lista.append(brd)
    context = {
        'query': lista
    }

    return render(request, 'collection/brand.html', context)

def brand_detail(request, slug):

    try:
        brand = get_object_or_404(Brand, slug = slug)
    except:

        raise ValueError(f'A marca "{slug}" não está cadastrada.')


    # bike_query = Bicycle.objects.filter(bike_brand_id = brand.id)
    bike_query = brand.bicycle_set.all()

    context = {
        'brand_obj' : brand,
        'bike_query':bike_query,
        'brand_slug':slug,
    }

    return render(request, 'collection/brand_detail.html', context)

def bike_detail(request, bike_slug, brandslug=None):
    
    try:
        bike = get_object_or_404(Bicycle, slug=bike_slug)

    except:
        bike = False

    context={
        'bike': bike,
    }

    return render(request, 'collection/bike_detail.html', context)
