from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# --------------------crearusuario----------------------------------------------------------------


def crear_usuario(request):

    if request.method == "GET":
        return render(request, "registrarce.html", {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:

            try:

                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return render(request, "portada.html")

            except:
                return render(
                    request,
                    "registrarce.html",
                    {"form": UserCreationForm, "error": "usuario ya exsiste"},
                )

    return render(
        request,
        "registrarce.html",
        {"form": UserCreationForm, "error": "contraseña no son iguales "},
    )


# ------------------------------------------------------------------------------------------------------


def logeo_deslogeo(request):
    logout(request)
    return redirect(request, "portada.html")


# --------------------editar contraseña----------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------

# --------------------editar nombre de usuario----------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------
# -----------------iniciar cesion  de usuario ------------------------------------------------------------------
def iniciarsecion(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        return render(request, "login.html", {"form": AuthenticationForm})
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:

            return render(
                request,
                "login.html",
                {"form": UserCreationForm, "error": "contraseña "},
            )
        else:
            login(request, user)

        # return redirect(request,"portada.html",{'form':UserCreationForm, "error":'contraseña '})

    return render(
        request,
        "registrarce.html",
        {"form": UserCreationForm, "error": "contraseña no son iguales "},
    )
