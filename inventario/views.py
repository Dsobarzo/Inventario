from django.shortcuts import render, redirect
from .models import Inventario

# Create your views here.
def home(request):
    inventario = Inventario.objects.all()
    return render(request, "gestionInventario.html", {"inventario": inventario})

def registrarProducto(request):
    codigo =request.POST['numCodigo']
    nombre = request.POST['txtNombre']
    tipo = request.POST['txtTipo']

    producto = Inventario.objects.create(
        codigo=codigo, nombre=nombre, tipo=tipo)
    return redirect('/')

def eliminarProducto(request, codigo):
    producto = Inventario.objects.get(codigo=codigo)
    producto.delete()
    return redirect('/')

def edicionProducto(request, codigo):
    producto = Inventario.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"producto": producto})

def editarProducto(request):
    codigo = request.POST['numCodigo']
    nombre = request.POST['txtNombre']
    tipo = request.POST['txtTipo']

    producto = Inventario.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.tipo = tipo
    producto.save()
    return redirect('/')


