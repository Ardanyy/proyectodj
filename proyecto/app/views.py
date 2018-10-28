from django.shortcuts import render,get_object_or_404
from .models import Juego,Slider,Distribuidora,Genero,Plataformas

def distribuidora(request,id):
    distribuidora = get_object_or_404(Distribuidora,id=id)
    return render(request,"core/distribuidoras.html",{'distribuidora':distribuidora})

def generos (request,id):
    genero = get_object_or_404(Genero,id=id)
    return render(request,"core/genero_detalle.html",{'genero':genero})


def geneross (request):
    genero = Genero.objects.all()
    return render(request,"core/genero.html",{'genero':genero})


def plataforma (request):
    plataforma = Plataformas.objects.all()
    return render(request,"core/plataforma.html",{'plataforma':plataforma})

def plataformas (request,id):
    plataforma = get_object_or_404(Plataformas,id=id)
    juego= Juego.objects.all()
    return render(request,"core/plataforma_detalle.html",{'plataforma':plataforma,'juego':juego})

def inicio(request):
     juego = Juego.objects.all()
     slider = Slider.objects.all()
     distribuidor = Distribuidora.objects.all()
     return render(request,"core/index.html",{'slider':slider,'juego':juego,'distribuidor':distribuidor})

def juego(request):
     juego = Juego.objects.all()
     return render(request,"core/juego.html",{'juego':juego})

def detalle(request,id):
     juego = get_object_or_404(Juego,id=id)
     genero = Genero.objects.all()
     distribuidor = Distribuidora.objects.all()
     return render(request,"core/detalle.html",{'juego':juego,'genero':genero,'distribuidor':distribuidor})
# Create your views here.
