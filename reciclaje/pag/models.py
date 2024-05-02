from django.db import models

# Create your models here.
class Desechos(models.Model):
    
    clasificacion = models.CharField(max_length=30)
    preciokg = models.FloatField()
    
    def __str__(self):
        return f"{self.clasificacion}"


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

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    

class Venta(models.Model):
    EstadoP = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Descompuesto', 'Descompuesto')
    ]
    Marcas = [
    ('Samsung', 'Samsung'),
    ('LG', 'LG'),
    ('Lenovo', 'Lenovo'),
    ('Apple', 'Apple'),
    ('Sony', 'Sony'),
    ('Microsoft', 'Microsoft'),
    ('Google', 'Google'),
    ('Huawei', 'Huawei'),
    ('Dell', 'Dell'),
    ('HP', 'HP'),
    ('Acer', 'Acer'),
    ('Asus', 'Asus'),
    ]

    tipo = models.ForeignKey(Desechos, on_delete=models.CASCADE)
    marca = models.CharField(max_length=13, choices=Marcas)
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