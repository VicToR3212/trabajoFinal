# ACA SE VA CREAR UN FORMULARIO BASADO A LOS DATOS QUE SE DESEAN EN EL FORMULARIO
from django import forms
from .models import Publicacion, Categoria


class CrearpublicacionForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    review = forms.CharField(widget=forms.TextInput())
    genero = forms.CharField(widget=forms.TextInput())
    categoria = forms.ModelChoiceField(
        label="categoria", queryset=Categoria.objects.all()
    )
    imagen = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Publicacion
        # esta instrucion hace referencia a todos los atribuos
        fields = ["nombre", "review", "genero", "Categoria", "imagen"]
        help_texts = {k: "" for k in fields}


class ediatarblicacionForm(forms.Form):

    class Meta:
        model = Publicacion
        # esta instrucion hace referencia a todos los atribuos
        fields = ["nombre", "review", "genero", "Categoria", "imagen"]
        help_texts = {k: "" for k in fields}


class AñadirCategoriaForm(forms.Form):
    # email=forms.EmailField(widget=forms.EmailField(attrs={'pleaceholder':'password','class':'login_input'}))
    usuario = forms.CharField(
        widget=forms.TextInput({"pleaceholder": "email", "class": "login_input"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"pleaceholder": "password", "class": "login_input"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"pleaceholder": "password", "class": "login_input"}
        )
    )

    class Meta:
        model = Categoria
        # esta instrucion hace referencia a todos los atribuos
        fields = ["correo", "password1"]
        help_texts = {k: "" for k in fields}
