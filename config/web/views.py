from django.shortcuts import render
from web.formularios.platos import FormularioPlatos
from web.formularios.empleados import FormularioEmpleados

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Plato(request):

    # Esta vista va a utilizar un formulario de django
    formulario = FormularioPlatos()

    # Creamos un diccionario para enviar el formulario al HTML
    data = {
        'formulario': formulario
    }
    return render(request, 'menuPlatos.html', data)

def Empleado(request):
    formulario = FormularioEmpleados()
    data = {
        'formulario': formulario
    }
    return render(request, 'registrarEmpleados.html', data)
