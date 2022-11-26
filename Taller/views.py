from django.shortcuts import render
from django.http import HttpResponse 
from Taller.forms import ClienteForm, CodigorepuestoForm
from Taller.models import Clientes, Codigorepuestos




def cliente(request):

    cliente1=Clientes(nombre="Esteban",apellido="Fernandez",direccion="Argumedo 3550",numero=1345465)
    
    cliente.save()
    cadena_Texto="cliente guardado: "+cliente1.nombre +" "+str(cliente1.apellido)+" "+str(cliente1.direccion)+" "+str(cliente1.numero)
    return HttpResponse(cadena_Texto)
     

def inicio(request):
    

    return render (request, "Taller/inicio.html")


def clientes(request):
    return render (request, "Taller/clientes.html")

def proveedores(request):
    return render (request, "Taller/proveedores.html")

def codigorepuestos(request):

    if request.method=="POST":
        form=CodigorepuestoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            numero=informacion["numero"]
            uso=informacion["uso"]
            descripcion=informacion["descripcion"]
            
            repuesto= Codigorepuestos(numero=numero, uso=uso, descripcion=descripcion)
            repuesto.save()
            return render (request, "Taller/inicio.html", {"mensaje": "Repuesto esta creado correctamente!!"})
    else:
        formulario=CodigorepuestoForm()


    return render (request, "Taller/codigorepuestos.html", {"form":formulario})


def clienteFormulario(request):

    if request.method=="POST":
        form=ClienteForm(request.POST)
      
        if form.is_valid():
            informacion=form.cleaned_data
            nombrecito=informacion["nombre"]
            apellidito=informacion["apellido"]
            direccioncita=informacion["direccion"]
            numerito=informacion["numero"]  

            cliente1=Clientes(nombre=nombrecito,apellido=apellidito,direccion=direccioncita,numero=numerito)
            cliente1.save()
            return render (request, "Taller/inicio.html")
    else:
        formulario=ClienteForm()


    return render(request, "Taller/clienteFormulario.html", {"form":formulario})


def busquedaapellido(request):
    return render(request, "Taller/busquedaapellido.html")


def buscar(request):

    if request.GET["apellido"]:

        apellido=request.GET["apellido"]

        clientes=Clientes.objects.filter(apellido__icontains=apellido)
        return render(request,"Taller/resultadosBusqueda.html", {"clientes":clientes} )
    else:
        return render(request, "Taller/busquedaapellido.html", {"mensaje":" Ingrese un apellido"})


# Create your views here.
