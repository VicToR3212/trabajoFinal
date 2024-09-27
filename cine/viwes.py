from django.shortcuts import render


def crear(request):
    return render(request,"usuarioNuevo.html")


def cine(request):
    return render(request,"portada.html")


def secion(request):
    return render(request,"registrarce.html")

def publicacion(request):
    return render(request,"cine.html")
