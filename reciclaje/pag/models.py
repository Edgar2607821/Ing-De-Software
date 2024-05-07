from django.db import models

# Create your models here.
class Dispositivo(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class TipoDisp(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class Marca(models.Model):
    tipo = models.ForeignKey(TipoDisp, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre 

class Catalogo(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoDisp, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    preciokg = models.FloatField()

    def __str__(self):
        return f"{self.dispositivo} - {self.tipo} - {self.marca} - {self.modelo}"


class Cliente(models.Model):
    SEXO_CHOICES = [
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro')
    ]
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=9, choices=SEXO_CHOICES)
    estado = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    cp = models.CharField(max_length=7)
    calle = models.CharField(max_length=20)
    nExt = models.CharField(max_length=4)
    nInt = models.CharField(max_length=4)
    colonia = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    fechanacimiento = models.DateTimeField(auto_now_add=True)
    referencias = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Venta(models.Model):
    EstadoP = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Descompuesto', 'Descompuesto')
    ]

    tipo = models.ForeignKey(Catalogo, on_delete=models.CASCADE) # Catalogo
    marca = models.CharField(max_length=13)                      
    Modelo = models.CharField(max_length=20) 
    AnioFab = models.DateField() 
    fecha = models.DateTimeField(auto_now_add=True)
    EstadoP = models.CharField(max_length=13, choices=EstadoP)
    descripcion = models.TextField()
    peso = models.FloatField()

    def __str__(self):
        return f"{self.Tipo} {self.Marca}"


#tipo 
#dispositivo