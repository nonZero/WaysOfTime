from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from viewer.models import Maps, MyMaps


def index(request):
    '''
    This is the index views.
    '''
    return render(request, 'index.html')


def getImage(request, img_id):
    '''
    get an image url to place on the page when thumbnail is clicked
    '''
    my_map = Maps.objects.filter(id__contains=img_id)

    url = "http://localhost:3000/maps/tile/{id}/{xyz}.png"

    response = JsonResponse([{
        'id': my_map[0].id,
        'title': my_map[0].title,
        'url': url.format(id=my_map[0].id, xyz='{z}/{x}/{y}'),
        'year': my_map[0].date_depicted,
        'author': my_map[0].authors
    }], safe=False)

    return response

def map_detail(request, map_id):
    '''
    '''
    map = MyMaps.objects.get(map_id=map_id)
    return render(request, 'layouts/map_page.html', {'map':map})
