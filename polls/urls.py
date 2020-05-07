from django.conf.urls import url
from django.urls import path

from . import views

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

    url('apiaries_list/', views.Apiaries_list, name='apiaries_list'),

    path('apiaries_form/', views.Apiaries_form, name='apiaries_form'),

    path('hives_list/', views.Hives_list, name='hives_list'),

    path('hives_form/', views.Hives_form, name='hives_form'),
    
    url('checks_list/', views.Checks_list, name='checks_list'),

    path('checks_form/', views.Checks_form, name='checks_form'),


]