from django.db import models





class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    numero=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.direccion+" "+str(self.numero)



class Proveedores(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    numero= models.IntegerField()

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.email+" "+str(self.numero)
        

class Codigorepuestos(models.Model):
    numero= models.IntegerField()
    uso= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.numero)+" "+self.uso+" "+self.descripcion


