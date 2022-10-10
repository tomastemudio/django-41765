from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random

from home.models import Humano

def hola(request):
    return render(request, "home/hola.html",{})

def fecha(request):
    fecha_y_hora = datetime.now()
    mostrar_fecha = f'La fecha y hora actual es {fecha_y_hora}'
    return render(request, "home/fecha.html", {'mostrar': mostrar_fecha})

def calcular_fecha_nacimiento(request,edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años seria: {fecha}')

def mi_template(request):

    cargar_archivo = open(r'/Users/tomastemudio/Desktop/Python_Coder/proyectoClases/home/templates/mi_template.html', 'r')

    template = Template(cargar_archivo.read())  #.read() para que el archivo sea un string.
    cargar_archivo.close

    contexto = Context()

    template_renderizado = template.render(contexto)


    return HttpResponse(template_renderizado)

def tu_template(request,nombre):

    # cargar_archivo = open(r'/Users/tomastemudio/Desktop/Python_Coder/proyectoClases/templates/tu_template.html', 'r')
    # template = Template(cargar_archivo.read())  
    # cargar_archivo.close
    # contexto = Context({'persona': nombre})
    # template_renderizado = template.render(contexto)

    template = loader.get_template('home/tu_template.html')           ## Nencesitamos indicarle al loader donde estan los archivos en el settings.py.
    template_renderizado = template.render({'persona': nombre})

    return HttpResponse(template_renderizado)

def prueba_template(request):

    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11),
        }

    template = loader.get_template('home/prueba_template.html')          
    template_renderizado = template.render(mi_contexto)

    return HttpResponse(template_renderizado)

def crear_persona(request): # Por defecto la vista de un formulario viene por GET. Para acceder por POST hay que hacer click en un button de formulario.

    # print('POST')
    # print(request.POST)  ## Es para que me de la informacion del POST.
    # print('==='*20)
    # print(request.method)
    # print('==='*20)

    if request.method == 'POST':    ## De esta manera puede guardar info en un POST y obtener info de un GET en la misma vista.
        nombre = request.POST.get('nombre')
        apellido = request.POST['apellido']
        persona = Humano(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_creacion=datetime.now())
        persona.save() ## Me guarda la persona en la base de datos.

        return redirect('ver_personas')  ## Me lleva directo a 'Ver personas'.

    return render(request, 'home/crear_persona.html', {})

def ver_personas(request):

    personas = Humano.objects.all()      ## Le pedimos a la base de datos todos los objetos de Humano.

    # template = loader.get_template('ver_personas.html')          
    # template_renderizado = template.render({'personas': personas})

    # return HttpResponse(template_renderizado)

    return render(request, 'home/ver_personas.html', {'personas': personas})

def index(request):

    return render(request, 'home/index.html')