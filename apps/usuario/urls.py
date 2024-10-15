from django.urls import path
from .views import crear_usuario, iniciarsecion

app_name = "apps.usuario"

urlpatterns = [
    path("crear/", crear_usuario, name="crear_usuario"),
    path("iniciarcesion/", iniciarsecion, name="iniciarsecion"),
]
