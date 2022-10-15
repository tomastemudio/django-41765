from django import forms

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length = 20)
    tipo = forms.CharField(max_length = 20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
