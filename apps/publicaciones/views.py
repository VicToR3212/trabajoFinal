from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
from .forms import CrearpublicacionForm
from .models import Publicacion


# -----------------------------   CREAR PUBLICACION-----------------
def crear_publicacion(request):

    form = CrearpublicacionForm()

    if request.method == "POST":
        form = CrearpublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = Publicacion()
            print("valido")
            print(request.POST)
            publicacion.nombre = form.cleaned_data["nombre"]
            publicacion.review = form.cleaned_data["review"]
            publicacion.genero = form.cleaned_data["genero"]
            publicacion.categoria = form.cleaned_data["categoria"]
            publicacion.imagen = form.cleaned_data["imagen"]

            publicacion.save()
            return redirect("apps.publicaciones:mostrarTodo_publicacion")
        else:
            print("invalido")

    contexto = {"form": form}
    return render(request, "publicar.html", {"form": form})


# -----------------------------   MOSTRAR TODOO PUBLICACION-----------------


def mostrarTodo_publicacion(request):

    if request.method == "POST":
        return render(request, "portada.html", {"peliculas": Publicacion.objects.all()})

    return render(request, "portada.html", {"peliculas": Publicacion.objects.all()})


# -----------------------------   MOSTRAR PUBLICACION-----------------


def mostrar_publicacion(request, pk):

    publicacion = Publicacion.objects.get(pk=pk)
    print(pk)
    return render(request, "ver.html", {"publicacion": publicacion})


# -----------------------------   EDITAR PUBLICACION-----------------


def editar_publicacion(request, pk):

    publicacion = Publicacion.objects.get(pk=pk)

    form = CrearpublicacionForm(
        initial={
            "nombre": publicacion.nombre,
            "review": publicacion.review,
            "genero": publicacion.genero,
            "categoria": publicacion.categoria,
            "imagen": publicacion.imagen,
        }
    )
    data = {"form": CrearpublicacionForm(request.POST)}
    if request.method == "POST":
        form = CrearpublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            print("valido")
            print(request.POST)
            publicacion.nombre = form.cleaned_data["nombre"]
            publicacion.review = form.cleaned_data["review"]
            publicacion.genero = form.cleaned_data["genero"]
            publicacion.categoria = form.cleaned_data["categoria"]
            publicacion.imagen = form.DateField["imagen"]

            publicacion.save()

            return redirect("apps.publicaciones:mostrarTodo_publicacion")
        else:
            print("invalido")

    contexto = {"form": form}
    return render(request, "publicar.html", {"form": form})


# -----------------------------   eliminar PUBLICACION-----------------


def eliminar_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    ima=publicacion.nombre
    ruta="media/"+str(publicacion.imagen)
    publicacion.delete()
    import os 
    os.remove(ruta)
    return redirect("apps.publicaciones:mostrarTodo_publicacion")
