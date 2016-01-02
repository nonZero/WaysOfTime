from django.shortcuts import render
from django.http import JsonResponse
from viewer.models import Maps
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import os


def getLayer(request, img_id):
    '''
    get an image url to place on the page when thumbnail is clicked
    '''
    map = Maps.objects.filter(id__contains=img_id)[0]

    url = "http://localhost:3000/uploads/{id}/thumb/{thumb_name_ext_stripped}.png"
    path = "/uploads/thumb/{thumb_name_ext_stripped}.png"
    val_dict = {}

    thumb_file_name, ext = os.path.splitext(map.upload_file_name)

    val_dict['id'] = map.id
    val_dict['title'] = map.title

    val_dict['thumb_url'] = url.format(id=map.id,thumb_name_ext_stripped=thumb_file_name)
    val_dict['thumb_path'] = path.format(id=map.id, thumb_name_ext_stripped=thumb_file_name)

    return render(request, 'layouts/layer_item.html',val_dict)


@ensure_csrf_cookie
def getGeoThumbs(request):
    '''
    get all images inside lat lngs area
    '''
    lenlat = request.POST.getlist('lenlat[]')
    left_down = lenlat[0]
    left_up = lenlat[1]
    right_up = lenlat[2]
    right_down = lenlat[3]
    maps = Maps.objects.all()

    for map in maps:
        new_map = map.bbox.split(',')
        print new_map[0] + "=====" + left_down + "-----"
        print new_map[1] + "=====" + left_up + "-----"
        print new_map[2] + "=====" + right_up + "-----"
        print new_map[3] + "=====" + right_down + "-----"
        print "xxxxxxxxxxxx"

    # correct_thing = Thing.object.get(name = "Hello")
    # random: things = Things.object.all().orderby('?')

    return HttpResponse('Success')
