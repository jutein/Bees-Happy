from django.conf.urls import include, url
from django.urls import path
from . import views
from .import serializers
from rest_framework import routers, viewsets
from django.contrib.auth.models import User


router = routers.DefaultRouter()
router.register(r'apiaries', views.Apiaries_APIViewSet)
router.register(r'hives', views.Hives_APIViewSet)
router.register(r'checks', views.Checks_APIViewSet)


app_name = 'polls'
urlpatterns = [

    url(r'^connexion$', views.connexion, name='connexion'),

    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),

    url(r'^$', views.entree, name='entree'),

    url(r'^(?P<toto>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<id_hive>[0-9]+)/results/$', views.results, name='results'),

    url(r'^(?P<id_hive>[0-9]+)/mesures/$', views.mesures, name='mesures'),

    url('Util/', views.Util),

    url('ok/', views.Ok),

    url('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('a/', views.Apiaries_APIList),
    path('h/', views.Hives_APIList),
    path('c/', views.Checks_APIList),
#path('', include('polls.urls')),

    url('apiaries_list/', views.Apiaries_list, name='apiaries_list'),

    path('apiaries_form/', views.Apiaries_form, name='apiaries_form'),

    path('hives_list/', views.Hives_list, name='hives_list'),

    path('hives_form/', views.Hives_form, name='hives_form'),
    
    url('checks_list/', views.Checks_list, name='checks_list'),

    path('checks_form/', views.Checks_form, name='checks_form'),


]