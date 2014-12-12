from django import forms


class AnamnesisForm(forms.Form):
    diabetes = forms.BooleanField(required=False)
    hipertension = forms.BooleanField(required=False)
    cancer = forms.BooleanField(required=False)
    alergias = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese alergias separadas por una coma'}))


class ExamenBucalForm(forms.Form):
    caries = forms.BooleanField()
    estado_ginvival = forms.CharField(max_length=50)
    anomalia_dento_maxilofacial = forms.CharField(max_length=50)
    mucosa_de_mejilla = forms.CharField(max_length=50)
    lengua = forms.CharField(max_length=50)
    frenillo_lingual = forms.CharField(max_length=50)
    frenillo_labial_medio_superior = forms.CharField(max_length=50)
    frenillo_labial_inferior = forms.CharField(max_length=50)


class TratamientoForm(forms.Form):

    pieza = forms.IntegerField()
    material = forms.CharField(max_length=50)
    cara = forms.CharField(max_length=50)
    endodoncia = forms.CharField(max_length=50)
    protesis = forms.CharField(max_length=50)
    exodoncia = forms.CharField(max_length=50)
    destartraje = forms.CharField(max_length=50)
    protesis_removible = forms.CharField(max_length=50)