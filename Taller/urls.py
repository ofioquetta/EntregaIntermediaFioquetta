
from django.urls import path
from Taller.views import *

urlpatterns = [
    path("cliente/", cliente, name="cliente"),
    path("clientes/", clientes, name="clientes"),
    path("provvedores/", proveedores, name="proveedores"),
    path("codigorepuestos/", codigorepuestos, name="codigorepuestos"),
    path("", inicio, name="inicio"),
    path("clienteFormulario/", clienteFormulario, name="clienteFormulario"),
    path("busquedaapellido/", busquedaapellido, name="busquedaapeliido"),
    path("buscar/", buscar, name="buscar"),
]