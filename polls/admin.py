from django.contrib import admin
from .models import Settingg_app, User_Details, Apiaries, Hive, Check
from .models import Check_Hive, Metric_Hive, Metric_Env

# Register your models here.
admin.site.register(Settingg_app)


class UserAdmin(admin.ModelAdmin):
    list_display = ('u_firstname', 'u_name')
    list_filter = ('u_firstname', 'u_name')
    search_fields = ('u_firstname', 'u_name')


#admin.site.register(User, UserAdmin)


class ApiariesAdmin(admin.ModelAdmin):
    list_display = ('a_fkuser', 'a_name', 'a_idgateway')
    list_filter = ('a_fkuser', 'a_name', 'a_idgateway')
    search_fields = ('a_fkuser', 'a_name')
    fieldsets = (
       ('Info identification', {
            'classes': ['wide', ],
            'fields': ('a_id', 'a_fkuser')
        }),
       ('Info Rucher', {
            'classes': ['extrapretty', ],
            'fields': ('a_name',)
        }),
       ('Info Gateway', {
            'classes': ['extrapretty', ],
            'fields': ('a_idgateway',)
        }),
    )

admin.site.register(Apiaries, ApiariesAdmin)


class HiveAdmin(admin.ModelAdmin):
    list_display = ('h_fkapiary', 'rfid_id', 'h_boxdate')
    list_filter = ('h_fkapiary', 'rfid_id', 'h_boxdate')
    search_fields = ('h_fkapiary', 'rfid_id')
    fieldsets = (
       ('Info Rucher', {
            'classes': ['wide', ],
            'fields': ('h_fkapiary', 'rfid_id', 'h_boxdate')
        }),
       ('Info Ruche', {
            'classes': ['extrapretty', ],
            'fields': ('h_model', 'h_framenb')
        }),
    )

 
admin.site.register(Hive, HiveAdmin)


class CheckAdmin(admin.ModelAdmin):
    list_display = ('c_fkhive', 'c_datetime', 'c_globalstatus')
    list_filter = ('c_fkhive', 'c_datetime', 'c_globalstatus')
    search_fields = ('c_fkhive', 'c_datetime')
    fieldsets = (
       ('Info visite', {
            'classes': ['wide', ],
            'fields': ('c_datetime','c_fkhive',)
        }),
       ('Apperçu général', {
            'classes': ['extrapretty', ],
            'fields': ('c_globalstatus','c_swarmsigns','c_aggressive','c_sicknesssigns','c_sickness',)
        }),
       ('Examen détaillé', {
            'classes': ['extrapretty', ],
            'fields': ('c_foodframenb','c_foodquality','c_broodframenb','c_broodframequality','c_dronebrood','c_drone',)
        }),
       ('Info Reine', {
            'classes': ['extrapretty', ],
            'fields': ('c_queencellsnb','c_queencellsextract','c_queencelladded','c_queencellsdestroid',)
        }),
       ('Info Hausses', {
            'classes': ['extrapretty', ],
            'fields': ('c_super1','c_superstate1','c_super2','c_superstate2','c_super3','c_superstate3','c_super4','c_superstate4',)
        }),       
        ('Info Traitements', {
            'classes': ['extrapretty', ],
            'fields': ('c_traitment','c_tratmenttype',)
        }),
    )


admin.site.register(Check, CheckAdmin)


admin.site.register(Check_Hive)


class MhAdmin(admin.ModelAdmin):
    list_display = ('mh_fkhive', 'mh_date', 'mh_type', 'mh_measure')
    list_filter = ('mh_fkhive', 'mh_date', 'mh_type', 'mh_measure')
    search_fields = ('mh_fkhive', 'mh_date', 'mh_type')


admin.site.register(Metric_Hive, MhAdmin)


class MeAdmin(admin.ModelAdmin):
    list_display = ('me_fkapiariy', 'me_date', 'me_type')
    list_filter = ('me_fkapiariy', 'me_date', 'me_type')
    search_fields = ('me_fkapiariy', 'me_date', 'me_type')


admin.site.register(Metric_Env,MeAdmin)
