
from django.urls import path
from Taller.views import *

urlpatterns = [
    path("cliente/", clientes, name="cliente"),
    path("clientes/", clientes, name="clientes"),
    path("proveedores/", proveedores, name="proveedores"),
    path("codigorepuestos/", codigorepuestos, name="codigorepuestos"),
    path("", inicio, name="inicio"),
    path("clienteFormulario/", clienteFormulario, name="clienteFormulario"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar, name="buscar"),
    path("resultadosBusqueda/", buscar, name="resultadosBusqueda"),
    path("listadeclientes/", listadeclientes, name="listadeclientes"),
]