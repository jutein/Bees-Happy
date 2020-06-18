from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.conf import settings

User = settings.AUTH_USER_MODEL

# general app setting 
class Settingg_app(models.Model):
    as_appname = models.CharField(max_length=10,default='BEESHAPPY')

#user setting
class User_Details(models.Model):
    u_fkuser = models.ForeignKey(User, on_delete=models.CASCADE)
    u_id = models.AutoField(primary_key=True)
    u_firstname = models.CharField(max_length=20)
    u_name = models.CharField(max_length=20)
    u_mail = models.CharField(max_length=30,unique=True, null=False)
    u_telephone = models.CharField(max_length=15)
    u_etsname = models.CharField(max_length=20)
    u_etsadresse = models.CharField(max_length=50)
    u_etstown = models.CharField(max_length=30)
    u_estcountry = models.CharField(max_length=20)
    u_esttelephone = models.CharField(max_length=15)

#Apiaries linked many to one User
class Apiaries(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_fkuser = models.ForeignKey(User, on_delete=models.CASCADE)
    a_name = models.CharField(max_length=15)
    a_idgateway = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Mes rucher"
        ordering = ['a_idgateway']


class Apiarieform(ModelForm):
    #def __init__(self, *arg, **kwargs):
    #    iduser = kwargs.pop('id_user')
    #    super(Apiarieform, self).__init__(*args, **kwargs)
    class Meta:
        model = Apiaries
        fields = ['a_name', 'a_idgateway']
        #'a_fkuser',


#Hive linked many to one Apiary
class Hive(models.Model):
    HIVE_MODEL = (
        ('D','DADANT'),
        ('L','LANGSTROTH'),
        ('W','WARRE'),
        ('K','KENYANE'),
        ('V','VOIRNOT'),
        ('P','PAILLE'),
        ('A','AUTRE'),
    )
    rfid_id = models.IntegerField(default=99)
    h_fkapiary = models.ForeignKey(Apiaries, on_delete=models.CASCADE)
    h_boxdate = models.DateTimeField(auto_now=False,auto_now_add=False)
    h_model = models.CharField(max_length=10,choices=HIVE_MODEL)
    h_framenb = models.BigIntegerField(default=10)

    class Meta:
        verbose_name = "Mes ruches"
        ordering = ['rfid_id']


class Hiveform(ModelForm):
    class Meta:
        model = Hive
        fields = ['rfid_id', 'h_boxdate', 'h_model', 'h_framenb']

#Check linked many to one Hive (Visites)
class Check(models.Model):
    CHECK_STATUS = (
        ('E','EXCELLENT'),
        ('B','BON'),
        ('M','MOYEN'),
        ('A','MAUVAIS'),
    )
    CHECK_FOODQUALITY = (
        ('M','MAXIMUM'),
        ('S','SUFFISANTE'),
        ('O','MOYENNE'),
        ('C','A COMPLETER'),
        ('V','VIDE'),
    )
    CHECK_BRQUAL = (
        ('F','TRES REMPLI'),
        ('C','COMPLET'),
        ('N','NORMAL'),
        ('P','PARTIEL'),
        ('V','VIDE'),
    )
    CHECK_DRONEBROOD = (
        ('E','EXCES'),
        ('N','NORMAL'),
        ('A','FAIBLE'),
    )
    CHECK_TRAITMENT = (
        ('A','APIVAR'),
        ('X','XXX'),
        ('Y','YYY'),
    )
    CHECK_SICKNESS = (
        ('V','VARROA'),
        ('L','LOQUE AMERICAINE'),
        ('R','RRRR'),
    )
    CHECK_SUPERQUALITY = (
        ('P','PLEIN'),
        ('M','MOYEN'), 
        ('V','VIDE'),
    )
    QUEEN_TYPE = (
        ('CA','CAUCASE'),
        ('NO','NOIRE'),
        ('IN','INCONNUE'),
        ('XX','XXXX'),
    )
    QUEEN_COLOR = (
        ('B','BLUE'),
        ('W','WHITE'),
        ('Y','YELLOW'),
        ('R','RED'),
        ('G','GREEN')
    )
    #c_id = models.IntegerField(primary_key=True)
    c_datetime = models.DateTimeField(blank=True)
    c_fkhive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    c_globalstatus = models.CharField(max_length=10, choices=CHECK_STATUS)
    c_swarmsigns = models.BooleanField(default=False)
    c_foodframenb = models.IntegerField(default=0, blank=True)
    c_foodquality = models.CharField(max_length=15, choices=CHECK_FOODQUALITY, blank=True)
    c_broodframenb = models.IntegerField(default=3, blank=True)
    c_broodframequality = models.CharField(max_length=15, choices=CHECK_BRQUAL, blank=True)
    #c_queendate = models.DateTimeField(auto_now=False,auto_now_add=False)
    #c_queentype = models.CharField(max_length=10,choices=QUEEN_TYPE)
    #c_queencolor = models.CharField(max_length=6, choices=QUEEN_COLOR)
    c_queencellsnb = models.IntegerField(default=0)
    c_queencellsextract = models.IntegerField(default=0)
    c_queencelladded = models.IntegerField(default=0)
    c_queencellsdestroid = models.IntegerField(default=0)
    c_aggressive = models.BooleanField(default=False)
    c_dronebrood = models.CharField(max_length=10, choices=CHECK_DRONEBROOD, blank=True)
    c_drone = models.CharField(max_length=10, choices=CHECK_DRONEBROOD, blank=True)
    c_traitment = models.BooleanField(default=False)
    c_tratmenttype = models.CharField(max_length=15, choices=CHECK_TRAITMENT, blank=True)
    c_sicknesssigns = models.BooleanField(default=False)
    c_sickness = models.CharField(max_length=15, blank=True)
    c_super1 = models.BooleanField(default=False)
    c_superstate1 = models.CharField(max_length=15, choices=CHECK_SUPERQUALITY, blank=True)
    c_super2 = models.BooleanField(default=False)
    c_superstate2 = models.CharField(max_length=15, choices=CHECK_SUPERQUALITY, blank=True)
    c_super3 = models.BooleanField(default=False)
    c_superstate3 = models.CharField(max_length=15, choices=CHECK_SUPERQUALITY, blank=True)
    c_super4 = models.BooleanField(default=False)
    c_superstate4 = models.CharField(max_length=15, choices=CHECK_SUPERQUALITY, blank=True)

    class Meta:
        verbose_name = "Mes visites"
        ordering = ['c_datetime']


class Checkform(ModelForm):
    class Meta:
        model = Check
        fields = '__all__'

class Check_Hive(models.Model): #A supprimer
    rfid_hive = models.IntegerField(default=0)
    chk_date = models.DateTimeField(auto_now=True)
    etat_couvain = models.CharField(max_length=20)
    nb_cadrecouvain = models.IntegerField(default=0)
    queen_cells = models.IntegerField(default=0)
    add_queen_cell = models.BooleanField(default=0)
    Restiction = models.IntegerField(default=0)
    traitement = models.CharField(max_length = 15, blank=True)

    def __str__(self):
        return "Ruche N°"+str(self.rfid_hive)+" - "+str(self.chk_date)+" - "+self.etat_couvain



#Apiary Measurements linked many to one Apiary
class Metric_Env(models.Model):
    METRICENV_TYPE = (
        ('T','TEMP'),
        ('P','PRES'),
        ('R','RAIN'),
        ('L','LIGH'),
    )
    me_fkapiariy = models.ForeignKey(Apiaries, on_delete=models.CASCADE, to_field=None)
    me_date = models.DateTimeField(auto_now=True)
    me_measure = models.FloatField(default=0)
    me_type = models.CharField(max_length=1, choices=METRICENV_TYPE)

    class Meta:
        verbose_name = "Mesures des ruchers"
        ordering = ['me_date']

    def __str__(self):
        return "Rucher N°"+str(self.me_fkapiariy)+" - "+str(self.me_date)+" - mesure:"+str(self.me_measure) + " - Type mesure:"+self.me_type

#Hive measurements linked many to one Hive
class Metric_Hive(models.Model):
    METRIHIVE_TYPE = (
        ('T','TEMP'),
        ('P','PRES'),
        ('H','HUMI'),
        ('S','SOUN'),
    )
    #mh_id = models.IntegerField(primary_key=True)
    mh_fkhive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    mh_date = models.DateTimeField(auto_now=True)
    mh_measure = models.FloatField(default=0)
    mh_type = models.CharField(max_length=1, choices=METRIHIVE_TYPE)

    class Meta:
        verbose_name = "Mesures ruches"
        ordering = ['mh_date']

    def __str__(self):
        return "Ruche N°"+str(self.mh_fkhive)+" - "+str(self.mh_date)+" - mesure:"+str(self.mh_measure) + " - Type mesure:"+self.mh_type

    
