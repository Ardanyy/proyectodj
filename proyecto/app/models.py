from django.db import models
from django.utils import timezone
from django.contrib import admin

class Controles(models.Model):
        nombre  = models.CharField(max_length=200, verbose_name="Nombre")
        descripcion  = models.CharField(max_length=200, verbose_name="Descripcion")
        created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
        updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
        published_date=models.DateTimeField(blank=True, null=True)
        class Meta:
                verbose_name="Controles" 
                verbose_name_plural="Controles"
                ordering = ["-created"]

        def __str__(self): #devuelve el nombre del proyecto
                return self.nombre 

class Genero(models.Model):
        nombre  = models.CharField(max_length=200, verbose_name="Nombre")
        descripcion  = models.CharField(max_length=200, verbose_name="Descripcion")
        created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
        updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
        published_date=models.DateTimeField(blank=True, null=True)
        class Meta:
                verbose_name="Genero" 
                verbose_name_plural="Generos"
                ordering = ["-created"]

        def __str__(self): #devuelve el nombre del proyecto
                return self.nombre 

class Plataformas(models.Model):
        nombre  = models.CharField(max_length=200, verbose_name="Nombre")
        Foto  = models.ImageField(verbose_name="imagen",upload_to="app",null=True,blank=True)
        jubailidad = models.ManyToManyField(Controles,verbose_name="Controles",related_name="control")
        descripcion  = models.CharField(max_length=200, verbose_name="Descripcion")
        created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
        updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
        published_date=models.DateTimeField(blank=True, null=True)
        class Meta:
                verbose_name="Plataforma" 
                verbose_name_plural="Plataformas"
                ordering = ["-created"]

        def __str__(self): #devuelve el nombre del proyecto
                return self.nombre 

class Slider(models.Model):
        nombre  = models.CharField(max_length=200, verbose_name="Nombre")
        Foto  = models.ImageField(verbose_name="imagen",upload_to="app",null=True,blank=True)
        descripcion  = models.CharField(max_length=200, verbose_name="Descripcion")
        created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
        updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
        published_date=models.DateTimeField(blank=True, null=True)
        class Meta:
                verbose_name="Slider" 
                verbose_name_plural="Sliders"
                ordering = ["-created"]

        def __str__(self): #devuelve el nombre del proyecto
                return self.nombre 

class Distribuidora(models.Model):
        nombred  = models.CharField(max_length=200, verbose_name="Nombre")
        industria  = models.CharField(max_length=200, verbose_name="Industria")
        fundacion = models.CharField(max_length=200, verbose_name="fundacion")
        sede = models.CharField(max_length=200, verbose_name="sede")
        Foto  = models.ImageField(verbose_name="imagen",upload_to="app",null=True,blank=True)
        created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
        updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
        published_date=models.DateTimeField(blank=True, null=True)
        class Meta:
                verbose_name="Distribuidora" 
                verbose_name_plural="Distribuidoras"
                ordering = ["-created"]

        def __str__(self): #devuelve el nombre del proyecto
                return self.nombred 
                
class Juego(models.Model):
    nombre  = models.CharField(max_length=200, verbose_name="Nombre")
    creadores  = models.CharField(max_length=200, verbose_name="creadores")
    Foto  = models.ImageField(verbose_name="imagen",upload_to="app",null=True,blank=True)
    Descripcion  = models.CharField(max_length=200, verbose_name="Descripcion")
    distribuidora = models.ForeignKey(Distribuidora,on_delete=models.CASCADE,related_name="keyd")
    genero = models.ManyToManyField(Genero,verbose_name="Genero",related_name="keygenero")
    plataformas = models.ManyToManyField(Plataformas,verbose_name="Plataforma",related_name="keyplat")
    Descripcion=models.TextField(verbose_name="Descripcion")
    fecha_lanzamiento = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de lanzamiento")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    class Meta:
                verbose_name="Juego" 
                verbose_name_plural="Juegos"
                ordering = ["-created"]
 
    def __str__(self):
        return self.nombre

