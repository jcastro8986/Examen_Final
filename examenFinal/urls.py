from . import views
from django.urls import path

app_name = 'examenFinal'

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('info_Tarea',views.info_Tarea,name='info_Tarea'),
    path('agregar_Tarea',views.agregar_Tarea,name='agregar_Tarea'),
    path('eliminar_Tarea',views.eliminar_Tarea,name='eliminar_Tarea'),
    path('actualizar_Tarea',views.actualizar_Tarea,name='actualizar_Tarea'),
]