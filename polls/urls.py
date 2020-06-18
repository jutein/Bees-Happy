from django.conf.urls import include, url
from django.urls import path
from . import views
from .import serializers
from rest_framework import routers, viewsets
from django.contrib.auth.models import User

#************ API router ****************
router = routers.DefaultRouter()
router.register(r'apiaries', views.Apiaries_APIViewSet)
router.register(r'hives', views.Hives_APIViewSet)
router.register(r'checks', views.Checks_APIViewSet)


app_name = 'toto'
urlpatterns = [

    #url(r'^LoginView$', views.LoginView, name='LoginView'),

    #url(r'^LogoutView$', views.LogoutView, name='Logoutview'),

    #url(r'^$', views.entree, name='entree'),

    #url(r'^(?P<toto>[0-9]+)/$', views.detail, name='detail'),

    #url(r'^(?P<id_hive>[0-9]+)/results/$', views.results, name='results'),

    #url(r'^(?P<id_hive>[0-9]+)/mesures/$', views.mesures, name='mesures'),


    url('ok/', views.Ok),

    url('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('a/', views.Apiaries_APIList),
    path('h/', views.Hives_APIList),
    path('c/', views.Checks_APIList),


]