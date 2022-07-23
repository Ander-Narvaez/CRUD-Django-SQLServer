from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #ursl crud
    path('', login_required(views.mostrar), name='login'),
    path('datos', login_required(views.mostrar), name='mostrar'),
    path('datos/agregar', login_required(views.agregar_dato), name='agregar_dato'),
    path('datos/modificar/<int:id>', login_required(views.modificar_dato), name='modificar_dato'),
    path('datos/eliminar/<int:id>', login_required(views.eliminar_dato), name='eliminar_dato'),
]