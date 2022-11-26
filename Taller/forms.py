from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    telefono = forms.IntegerField()


class CodigorepuestoForm(forms.Form):
    numero = forms.IntegerField()
    uso = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=100)
