from django.urls import path
from .views import (crear_publicacion,
    mostrarTodo_publicacion,
    editar_publicacion,
    eliminar_publicacion,
    mostrar_publicacion,
)

app_name = "apps.publicaciones"

urlpatterns = [
    # crear una publicacion. localhost:8000/publicaciones/crear/
    path("crear/", crear_publicacion, name="crear_publicacion"),
    # mostrar todas las pulicaciones
    path("", mostrarTodo_publicacion, name="mostrarTodo_publicacion"),
    # mostrar una publicacion
    path("ver/<int:pk>", mostrar_publicacion, name="mostrar_publicacion"),
    # editar una publicacion
    path("editar/<int:pk>", editar_publicacion, name="editar_publicacion"),
    # eliminar una publicacion
    path("eliminar/<int:id>", eliminar_publicacion, name="eliminar_publicacion"),
]