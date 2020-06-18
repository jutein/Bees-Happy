# Create your views here.
import os
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Template, Context
from .models import Check_Hive, Metric_Hive, Metric_Env, Hive, Check, Apiaries, Settingg_app, User
from .form import Rucheform
from .form import Apiaryform
from .form import LoginForm
from .models import Checkform
from .models import Hiveform, Apiarieform
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework import permissions
from polls.serializers import Apiaries_Serializer, Hives_Serializer, Checks_Serializer
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Apiaries
from django.views import View

class LoginView(TemplateView):
    def post(self, request, **kwargs): 
        username = request.POST.get('username', False) 
        password = request.POST.get('password', False) 
        next = request.GET.get('next', '/')
        user = authenticate(username=username, password=password)  
        if user is not None and user.is_active: 
            login(request, user) 
        else :
            print("inconnu !!!")
        #    return redirect(settings.LOGOUT_REDIRECT_URL)
        return redirect(next)

    def get(self, request, **kwargs): 
        template_name = 'front/index.html'
        return render(request, template_name)


class LogoutView(TemplateView):

    def get(self, request, **kwargs):
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)


class RegisterView(TemplateView):
    def post(self, request, **kwargs): 
#        template_name = 'front/register.html'
        user = User.objects.create_user(request.POST.get('email', False), request.POST.get('email', False), request.POST.get('password', False))
        user.first_name=request.POST.get('first_name', False)
        user.last_name = request.POST.get('last_name', False)
        print(user.username)
        user.save()
        template_name = 'front/index.html'
        return render(request, template_name)

    def get(self, request, **kwargs): 
        template_name = 'front/register.html'
        return render(request, template_name)
    

#@login_required
def entree(request): 
    template = loader.get_template('index.html')
    print(request.user)
    if request.user is not None and request.user.is_authenticated:
        print(request.user.id)
        myuser = request.user.first_name+' '+request.user.last_name
    else: 
        print("Log sans user")
        myuser = ""
    context = {'myuser': myuser}
    return HttpResponse(template.render(context, request))

@login_required
def Apiaries_list(request):
    Apiaries_list = Apiaries.objects.filter(a_fkuser = request.user.id) 
    Apiaries_count = Apiaries_list.count()
    template = loader.get_template('apiaries_list.html')
    context = {'Apiaries_list': Apiaries_list, 'Apiaries_count': Apiaries_count}
    return HttpResponse(template.render(context, request))

#class Apiaries_Lst(ListView):
#    model = Apiaries
#    def get_queryset(self):
 #       Aqs = super().get_queryset()
#        print(self.request)
#        return Aqs.filter(a_fkuser=5)
    #def get(request, *args, **kwargs):
    #    print(request)
    #    Apiaries_list = Apiaries.objects.all()#filter(a_fkuser = request.user.id) 
    #    Apiaries_count = Apiaries_list.count()
    #    template = loader.get_template('apiaries_list.html')
    #    context = {'Apiaries_list': Apiaries_list, 'Apiaries_count': Apiaries_count}
    #    return context

@login_required
def Apiaries_form(request):
    print("NEW APIARIE")
    if (request.method == 'POST'):
        iduser = request.user.id
        apiarie = Apiaries(a_fkuser=request.user)
        formap = Apiarieform(request.POST, instance=apiarie)
        print("apiari post appal form")
        if formap.is_valid():
            print("apiari valide")
            print(request.user.id)
            formap.save()
            formap
            return HttpResponseRedirect('/apiaries_list/')
    else:
        formap = Apiarieform()
    return render(request, 'apiaries_form.html', locals())


@login_required
def Apiaries_view(request, apiarie_id):
    #query = request.GET.get('query')
    print("Id apiarie : " + str(apiarie_id))
    #if not query :
    #    print("Pas de référene de rucher")
    #else :
    myuser = request.user.first_name+' '+request.user.last_name
    print("GET "+apiarie_id + "User: " + str(request.user.id))
    apiarie = Apiaries.objects.get(a_id = apiarie_id, a_fkuser = request.user.id) 
    hives = Hive.objects.filter(h_fkapiary = apiarie.a_id)
    print(apiarie.a_name)
    Hive_count=hives.count()
    context = {
            'apiarie': apiarie, 
            'myuser': myuser,
            'hives' : hives,
            'Hive_count' : Hive_count,
    }
    template = loader.get_template('apiarie_view.html')
    return HttpResponse(template.render(context, request))
    return render(request, 'apiarie_view.html', locals())

@login_required
def Hives_list(request):
    Hive_list = Hive.objects.all() 
    Hive_count = Hive_list.count()
    template = loader.get_template('hives_list.html')
    context = {'Hive_list': Hive_list, 'Hive_count': Hive_count}
    return HttpResponse(template.render(context,request))

@login_required
def Hives_form(request, apiarie_id):
    if (request.method == 'POST'):
        hive = Hive(h_fkapiary=apiarie_id)
        formh = Hiveform(request.POST, instance=hive)
        if formh.is_valid():
            formh.save()
            return HttpResponseRedirect('/hives_list/')
    else:
#        query = request.GET.get('query')
#        apiarie_id = query
    #    template = loader.get_template('hives_form.html')
    #    context = {'apiarie_id': apiarie_id}
        formh = Hiveform(request.POST)
#    return HttpResponse(template.render(context, request))
    return render(request, 'hives_form.html/', locals())
    

@login_required
def Checks_list(request):
    Check_list = Check.objects.all()
    Check_nb = Check_list.count()
    template = loader.get_template('checks_list.html')
    context = {'Check_list': Check_list, 'Check_nb': Check_nb}
    return HttpResponse(template.render(context, request))

@login_required
def Checks_form(request):
    if (request.method == 'POST'):
        formc = Checkform(request.POST)
        if formc.is_valid():
            formc.save()
            return HttpResponseRedirect('/checks_list/')
    else:
        formc = Checkform()
    return render(request, 'checks_form.html', locals())



#.......... API Apiaries .............
class Apiaries_APIViewSet(viewsets.ModelViewSet):
    queryset = Apiaries.objects.all()
    serializer_class = Apiaries_Serializer
    permissions_classes = [permissions.IsAuthenticated]


def Apiaries_APIList(request):
    if request.method == 'GET':
        q_apiaries = Apiaries.objects.all()
        ser_apiaries = Apiaries_Serializer(q_apiaries, many=True)
        return JsonResponse(ser_apiaries.data, safe=False)


#.......... API Hives .............
class Hives_APIViewSet(viewsets.ModelViewSet):
    queryset = Hive.objects.all()
    serializer_class = Hives_Serializer 
    permissions_classes = [permissions.IsAuthenticated]


def Hives_APIList(request):
    if request.method == 'GET':
        q_hives = Hive.objects.all()
        ser_hives = Hives_Serializer(q_hives, many=True)
        return JsonResponse(ser_hives.data, safe=False)


#.......... API Ckeck .............
class Checks_APIViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = Checks_Serializer 
    permissions_classes = [permissions.IsAuthenticated]


def Checks_APIList(request):
    if request.method == 'GET':
        q_checks = Check.objects.all()
        ser_checks = Checks_Serializer(q_checks, many=True)
        return JsonResponse(ser_checks.data, safe=False)


def Ok(request):
    Result = 'Ok'
    template = loader.get_template('polls/ok.html')
    context = {'Result': Result}
    return HttpResponse(template.render(context,request))


def detail(request, toto):
    #mesures_list = Metric_Hive.objects.order_by('-acq_date')
    #template=loader.get_template('polls/detail.html')
    #context = {'mesures_list' : mesures_list}
    try:
        hive = Check_Hive.objects.get(id_hive=toto)
    except Check_Hive.DoesNotExist:
        raise Http404("Ruche inexistantantante")
    #hive = get_object_or_404(Check_Hive,pk=id_hive)
    return render(request, 'polls/detail.html', {'hive': hive})
    #return HttpResponse(template,render(context, request))
 
 #  return HttpResponse("Vous regardez  ruche %s." % id_hive)

def results(request, id_hive):
    response = "You're looking at the results of Hive check %s."
    return HttpResponse(response % id_hive)

def mesures(request, id_hive):
   # return HttpResponse("ID enregistrement mesure = %s." % id_hive)
    try:
        mesure = Metric_Hive.objects.get(id_hive=id_hive)
    except Metric_Hive.DoesNotExist:
        raise Http404("Mesures inexistantantantes")
    return render(request, 'polls/mesures.html',{'mesure':mesure})


def Util(request):    
    return render(request, 'polls/calc.html', locals())

def rucheforme(request):
    form = Rucheform(request.POST or None)
    if form.is_valid():
        envoi = True
    return render(request, 'polls/Rucheform.html', locals())


def apiaryform(request):
    form = Apiaryform(request.POST or None)
    if form.is_valid():
        envoi = True
    return render(request, 'polls/apiary.html', locals())



  