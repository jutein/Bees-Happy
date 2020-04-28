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


def check_list(request):
    latest_check_list = Check.objects.all() #Check_Hive.objects.order_by('id_hive')
    template = loader.get_template('polls/checks.html')
    context = {'latest_check_list': latest_check_list,}
    #return render(request ,'polls/index.html',context)
    return HttpResponse(template.render(context,request))


def hives(request):
    latest_hive_list = Check_Hive.objects.all() #Check_Hive.objects.order_by('id_hive')
    template = loader.get_template('polls/hives.html')
    context = {'latest_hive_list': latest_hive_list,}
    #return render(request ,'polls/index.html',context)
    return HttpResponse(template.render(context,request))
    # output = ' - '.join([q.etat_couvain for q in latest_hive_list])+':'#+str(.join([q.id_hive for q in latest_hive_list]))
    # return HttpResponse(output)
    # return HttpResponse("Bees Happy is happy to welcome you.")
    #hive_list = Check_Hive.objects.order_by('-chk_date')
    #Check_Hive.objects.all()
    #return render(request, 'polls/index.html', hive_list)

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


def calc(request, nb1, nb2):    
    add = nb1 + nb2
    mult = nb1 * nb2
    montexte = "ceci est un texte trop long"
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