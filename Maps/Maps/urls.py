"""Maps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from viewer import views

router = routers.DefaultRouter()
router.register(r'maps', views.MapsViewSet)
router.register(r'my_maps', views.MyMapsViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
    url(r'^mapProfile/(?P<map_id>[-\w]+)/$' , views.map_detail, name='map_detail'),
    url(r'^getMapById/(?P<img_id>[-\w]+)/$', views.getImage),
    url(r'^getThumbs/(?P<stringToSearch>[-\w.]+)/$', views.getThumbs),
    url(r'^getGeoThumbs/$', views.getGeoThumbs),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^getLayer/(?P<img_id>[-\w]+)/$',views.getLayer),
    url(r'^api/v1/', include(router.urls)),
]
