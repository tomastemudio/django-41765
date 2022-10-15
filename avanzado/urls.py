from django.urls import path
from avanzado import views

urlpatterns = [
    # Version con vistas comunes
    # path('mascotas/', views.ver_mascotas, name = 'ver_mascotas'),
    # path('mascotas/crear/', views.crear_mascotas, name = 'crear_mascotas'),
    # path('mascotas/editar/<int:id>', views.editar_mascota, name = 'editar_mascota'),
    # path('mascotas/eliminar/<int:id>', views.eliminar_mascota, name = 'eliminar_mascota')

    # Version con clases basadas en vistas
    path('mascotas/', views.ListaMascotas.as_view(), name = 'ver_mascotas'),
    path('mascotas/crear/', views.CrearMascotas.as_view(), name = 'crear_mascotas'),
    path('mascotas/editar/<int:pk>', views.EditarMascotas.as_view(), name = 'editar_mascota'), ## Necesita que le pasemos pk.
    path('mascotas/eliminar/<int:pk>', views.EliminarMascota.as_view(), name = 'eliminar_mascota')
]
