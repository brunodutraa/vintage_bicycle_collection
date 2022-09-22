from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Brand, Bicycle
import plotly.express as px
from plotly.offline import plot


def all_brands(request):
    lista = []
    bbrand_query = Brand.objects.all()

        # lista.append(brd)
    for brd in bbrand_query:
        # if brd.bicycle_set.all():
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



def plot_view(request):
    dados_x = [2011, '2019', '2020', '2021', 2025]
    dados_y = [10, 20, 5, 40, 50]

    #fig = px.line(x = dados_x, y = dados_y)
    fig = px.bar(x = dados_x, y = dados_y)
    fig2 = plot(fig, output_type='div')
    context = {
        'fig' : fig2,
    }

    return render(request, 'collection/plot_view.html', context)