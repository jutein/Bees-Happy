"""monsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""TEST  """
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from polls.views import LoginView, LogoutView, RegisterView, entree 
#, Apiaries_Lst
from polls.views import Apiaries_view
from polls.views import Apiaries_form, Hives_form, Checks_form
from polls.views import Apiaries_list, Hives_list, Checks_list, Util

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', LoginView.as_view()),
    url(r'^logout', LogoutView.as_view()),
    url(r'^register', RegisterView.as_view()),
    url(r'^$', entree, name='entree'),
    #url(r'^apiaries$', Apiaries_Lst.as_view()),
    url(r'^apiaries_list', Apiaries_list, name='apiaries_list'),
    url(r'^apiaries_form/$', Apiaries_form, name='Apiarie_form'),
    url(r'^apiaries_view/(?P<apiarie_id>[0-9]+)/$', Apiaries_view, name='apiaries_view'),
    url(r'^hives_list/', Hives_list, name='hives_list'),
    url(r'^hives_form/(?P<apiarie_id>[0-9]+)/$', Hives_form, name='Hives_form'),
    url(r'^checks_list/', Checks_list, name='checks_list'),
    url(r'^checks_form/', Checks_form, name='checks_form'),
    url(r'^Util/', Util),
    url(r'^api', include('polls.urls')),
]
