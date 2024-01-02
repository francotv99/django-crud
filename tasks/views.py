from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pais, Estado
from .forms import formPais, formEstado

def home(request):
    datos = Pais.objects.filter(isActive=True)
    if request.method == 'POST':
        formulario = formPais(request.POST)
        if formulario.is_valid():
            pais = formulario.save(commit=False)
            if not pais.codigo:
                pais.codigo = pais.id
            pais.save()
            return redirect('home')
    else:
        formulario = formPais()
    
    return render(request, 'home.html', {'form': formulario, 'datos': datos})

def editarpais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id)
    if request.method == 'POST':
        formulario = formPais(request.POST, instance=pais)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = formPais(instance=pais)
    return render(request, 'editar_pais.html', {'form': formulario, 'pais': pais})

def eliminarpais(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id, isActive=True)
    if request.method == 'POST':
        pais.isActive = False
        pais.save()
        return redirect('home')
    datos = Pais.objects.filter(isActive=True)
    formulario = formPais()
    return render(request, 'home.html', {'form': formulario, 'datos': datos})

def lista_estados(request, pais_id):
    pais = get_object_or_404(Pais, pk=pais_id, isActive=True)
    datos = Estado.objects.filter(idpais_id=pais_id, isActive=True)
    if request.method == 'POST':
        formulario = formEstado(request.POST)
        if formulario.is_valid():
            estado = formulario.save(commit=False)
            estado.idpais = pais
            if not estado.codigo:
                estado.codigo = estado.id
            estado.save()
            return redirect('estados', pais_id=pais_id)
    else:
        formulario = formEstado()
    return render(request, 'estados.html', {'form': formulario, 'datos': datos, 'pais': pais})

def editarestados(request, estado_id):
    estado = get_object_or_404(Estado, pk=estado_id)
    if request.method == 'POST':
        formulario = formEstado(request.POST, instance=estado)
        if formulario.is_valid():
            formulario.save()
            return redirect('estados', pais_id=estado.idpais.id)
    else:
        formulario = formEstado(instance=estado)
    return render(request, 'editar_estado.html', {'form': formulario, 'estado': estado})

def eliminarestado(request, estado_id):
    estado = get_object_or_404(Estado, pk=estado_id, isActive=True)
    if request.method == 'POST':
        estado.isActive = False
        estado.save()
        return redirect('estados', pais_id=estado.idpais.id)
    datos = Estado.objects.filter(idpais_id=estado.idpais_id, isActive=True)
    formulario = formEstado()
    return render(request, 'estados.html', {'form': formulario, 'datos': datos, 'pais': estado.idpais})
