from django.shortcuts import render

# Create your views here.

##LLAMADO DE LA PAGINA DENTRO DE LA FUNCION HOME PARA REDIRIGIRLA

def home(request):
    return render(request,"home.html")