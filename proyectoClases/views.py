from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template

def hola(request):
    return HttpResponse('<h1>Buenas clase 41765</h1>')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request,edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años seria: {fecha}')

def mi_template(request):

    cargar_archivo = open(r'/Users/tomastemudio/Desktop/Python_Coder/proyectoClases/templates/template.html', 'r')

    template = Template(cargar_archivo.read())  #.read() para que el archivo sea un string.
    cargar_archivo.close

    contexto = Context()

    template_renderizado = template.render(contexto)


    return HttpResponse(template_renderizado)

