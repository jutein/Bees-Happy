from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class Apiaryform(forms.Form):

#    a_id = models.IntegerField(primary_key=True)
#    a_fkuser = models.ForeignKey(User, on_delete=models.CASCADE)
    a_name = forms.CharField(max_length=15)
    a_idgateway = forms.CharField(max_length=15)



class Rucheform(forms.Form):

    id_hive = forms.IntegerField(label="Identifiant de la ruche",required=False)
    Etat_couvain = forms.CharField(max_length=20)
    Date_contrôle = forms.DateTimeField(widget=forms.DateInput)
    nb_cadre_couvain = forms.IntegerField(help_text="Entrez un nombre")
    queen_cells = forms.IntegerField()
    add_queen_cell = forms.BooleanField(required=False)
    Restiction = forms.IntegerField()
    traitement = forms.CharField(max_length=15)

    def clean_traitement(self):
        traitement = self.cleaned_data['traitement']
        if "APIVAR" in traitement:
            raise forms.ValidationError("L'APIVAR est interdit en bio")
        return traitement  

    def clean_Etat_couvain(self):
        Etat_couvain=self.cleaned_data['Etat_couvain']
        #nb_cadre_couvain=self.
        if nb_cadre_couvain.validate < 2 and  self.Etat_couvain.__str__ == "BON":
            raise forms.ValidationError("Etat bon incompatible avec nb ")
        return Etat_couvain


