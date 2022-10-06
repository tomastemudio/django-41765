from django.urls import path
from home import views  ## Es recomenadado hacerlo asi.
#from . import views   

urlpatterns = [
    path('', views.index, name='index'),
    path('hola/', views.hola, name='hola'),
    path('fecha/', views.fecha, name='fecha'),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    # path('mi-template/', views.mi_template, name='mi_template'),
    path('tu-template/<str:nombre>', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
]