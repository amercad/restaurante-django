from django.shortcuts import render

from web.formularios.platos import FormularioPlatos
from web.formularios.empleados import FormularioEmpleados

from web.models import Platos, Empleados

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Plato(request):

    platosConsultado = Platos.objects.all()

    # Esta vista va a utilizar un formulario de django
    formulario = FormularioPlatos()

    # Creamos un diccionario para enviar el formulario al HTML
    data = {
        'formulario': formulario,
        'isSave': False,
        'platos': platosConsultado
    }

    if request.method=="POST":
        datosFormulario=FormularioPlatos(request.POST)
        print(datosFormulario)
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data
            print(datosLimpios)
            platoNuevo = Platos(
                nombre = datosLimpios["nombre"],
                descripcion = datosLimpios["descripcion"],
                fotografia = datosLimpios["fotografia"],
                precio = datosLimpios["precio"],
                tipo = datosLimpios["tipo"]
            )

            try:
                platoNuevo.save()
                data['isSave'] = True
                print('Platos guardados')
            except Exception as error:
                print('Upss', error)


    return render(request, 'menuPlatos.html', data)

def ListaPalto(request):
    platosConsultado = Platos.objects.all()
    data = {
        'platos': platosConsultado
    }

    return render(request, 'listaPlatos.html', data)

def Empleado(request):
    formulario = FormularioEmpleados()
    data = {
        'formulario': formulario,
        'isSave': False
    }

    if request.method=="POST":
        datosFormularioEmpleado=FormularioEmpleados(request.POST)
        if datosFormularioEmpleado.is_valid():
            datosLimpios = datosFormularioEmpleado.cleaned_data
            empleadoNuevo = Empleados(
                nombre = datosLimpios["nombre"],
                apellidos = datosLimpios["apellidos"],
                fotografia = datosLimpios["fotografia"],
                cargo = datosLimpios["cargo"],
                salario = datosLimpios["salario"],
                contacto = datosLimpios["contacto"]
            )

            try:
                empleadoNuevo.save()
                data['isSave'] = True
                print('Empleado guardados')
            except Exception as error:
                print('Upss', error)

    return render(request, 'registrarEmpleados.html', data)
