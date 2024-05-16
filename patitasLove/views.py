from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'patitasLove/home.html')

def contacto(request):
    return render(request, 'patitasLove/contacto.html')

def registro(request):
    return render(request, 'patitasLove/registro.html')

def sesion(request):
    return render(request, 'patitasLove/sesion.html')

def carrito(request):
    return render(request, 'patitasLove/carrito.html')