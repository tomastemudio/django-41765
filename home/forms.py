from django import forms

class HumanoFormulario(forms.Form):
    nombre = forms.CharField(max_length = 30)
    apellido = forms.CharField(max_length = 30)
    edad = forms.ImageField()
    fecha_creacion = forms.DateField(required=False) ## Dice que el campo de fecha de creacion del formulario no sea requerido.