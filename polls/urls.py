from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [

    url(r'^connexion$', views.connexion, name='connexion'),

    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),

    url(r'^$', views.entree, name='entree'),

    url('checks', views.check_list),

    url(r'^(?P<toto>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<id_hive>[0-9]+)/results/$', views.results, name='results'),

    url(r'^(?P<id_hive>[0-9]+)/mesures/$', views.mesures, name='mesures'),

    path('hives/',views.hives),

    path('calc/<int:nb1>/<int:nb2>/', views.calc),

    path('rucheform/', views.rucheforme, name='rucheform'),
    
    path('apiary/', views.apiaryform, name='apiary'),

]