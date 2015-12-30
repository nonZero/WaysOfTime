from django.shortcuts import render
from django.http import JsonResponse
from viewer.models import Maps
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
    pass
    # tasks = request.POST.getlist('lenlat[]')
    # params = request.POST.getlist('lng_lat[]')
    # maps = Maps.objects.all()
    # img_id = 1
    # map = Maps.objects.filter(id__contains=img_id)
    #
    # url = "http://localhost:3000/uploads/{id}/thumb/{thumb_name_ext_stripped}.png"
    # path = "/uploads/thumb/{thumb_name_ext_stripped}.png"
    # val_dict = {}
    #
    # thumb_file_name, ext = os.path.splitext(map.upload_file_name)
    #
    # val_dict['id'] = map.id
    # val_dict['title'] = map.title
    #
    # val_dict['thumb_url'] = url.format(id=map.id,thumb_name_ext_stripped=thumb_file_name)
    # val_dict['thumb_path'] = path.format(id=map.id, thumb_name_ext_stripped=thumb_file_name)
    # return render(request, 'layouts/layer_item.html', val_dict)
