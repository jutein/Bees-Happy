# Create your views here.
from django.http import Http404
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Check_Hive, Metric_Hive, Metric_Env, Hive, Check, Apiaries, Settingg_app, User
from .form import Rucheform
from .form import Apiaryform
from .form import ConnexionForm
from .models import Checkform
from .models import Hiveform, Apiarieform
from django.contrib.auth import authenticate, login

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())


def deconnexion(request):
    logout(request)
    return render(request, 'deconnection.html', locals())
    #from django.core.exceptions import ObjectDoesNotExist


def Checks_list(request):
    Check_list = Check.objects.all()
    Check_nb = Check_list.count()
    template = loader.get_template('polls/checks_list.html')
    context = {'Check_list': Check_list, 'Check_nb': Check_nb}
    return HttpResponse(template.render(context, request))


def Checks_form(request):
    if (request.method == 'POST'):
        formc = Checkform(request.POST)
        if formc.is_valid():
            formc.save()
            return HttpResponseRedirect('/polls/checks_list/')
    else:
        formc = Checkform()
    return render(request, 'polls/checks_form.html', locals())


def Hives_list(request):
    Hive_list = Hive.objects.all() 
    Hive_count = Hive_list.count()
    template = loader.get_template('polls/hives_list.html')
    context = {'Hive_list': Hive_list, 'Hive_count': Hive_count}
    return HttpResponse(template.render(context,request))


def Hives_form(request):
    if (request.method == 'POST'):
        formh = Hiveform(request.POST)
        if formh.is_valid():
            formh.save()
            return HttpResponseRedirect('/polls/hives_list/')
    else:
        formh = Hiveform()
    return render(request, 'polls/hives_form.html', locals())


def Apiaries_list(request):
    Apiaries_list = Apiaries.objects.all() 
    Apiaries_count = Apiaries_list.count()
    template = loader.get_template('polls/apiaries_list.html')
    context = {'Apiaries_list': Apiaries_list, 'Apiaries_count': Apiaries_count}
    return HttpResponse(template.render(context, request))


def Apiaries_form(request):
    if (request.method == 'POST'):
        formap = Apiarieform(request.POST)
        if formap.is_valid():
            formap.save()
            return HttpResponseRedirect('/polls/apiaries_list/')
    else:
        formap = Apiarieform()
    return render(request, 'polls/apiaries_form.html', locals())


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


def entree(request):    
    return render(request, 'polls/entree.html')


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



#def create_metric(request, id_hive):
#    hive = get_object_or_404(Check_Hive, pk=id_hive)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'polls/detail.html', {
#            'question': question,
 #           'error_message': "You didn't select a choice.",
 #       })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))    