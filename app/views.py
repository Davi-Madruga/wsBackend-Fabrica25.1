from django.shortcuts import render, redirect
from .models import Usuario, Instrument
from .forms import UsuarioForm, InstrumentForm


#USUARIOS#

def criar_view(request):
    if request.method == 'GET':
        form = UsuarioForm()
        return render(request, 'app/criar.html', {'form': form})
    elif request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:listar')

def listar_view(request):
    usuarios = Usuario.objects.all()
    return render(request, 'app/listar.html', {'usuarios': usuarios})

def editar_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
        return render(request, 'app/editar.html', {'form': form, 'usuario': usuario})
    elif request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('app:detalhar', pk=pk)

def deletar_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'app/deletar.html', {'usuario': usuario})
    elif request.method == 'POST':
        usuario.delete()
        return redirect('app:listar')

def detalhar_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if usuario:
        return render(request, 'app/detalhar.html', {'usuario': usuario})

#INSTRUMENTS/OBJETOS#

def criar_objeto(request):
    if request.method == 'GET':
        form = InstrumentForm()
        return render(request, 'app/criar_objeto.html', {'form': form})
    elif request.method == 'POST':
        form = InstrumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:listar_objeto')
        
def listar_objeto(request):
    instrumento = Instrument.objects.all()
    return render(request, 'app/listar_objeto.html', {'instrumento': instrumento})

def editar_objeto(request, pk):
    instrumento = Instrument.objects.get(pk=pk)
    if request.method == 'GET':
        form = InstrumentForm(instance=instrumento)
        return render(request, 'app/editar_objeto.html', {'form': form, 'instrumento': instrumento})
    elif request.method == 'POST':
        form = InstrumentForm(request.POST, instance=instrumento)
        if form.is_valid():
            form.save()
            return redirect('app:detalhar_objeto', pk=pk)

def deletar_objeto(request, pk):
    instrumento = Instrument.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'app/deletar_objeto.html', {'instrumento': instrumento})
    elif request.method == 'POST':
        instrumento.delete()
        return redirect('app:listar_objeto')

def detalhar_objeto(request, pk):
    instrumento = Instrument.objects.get(pk=pk)
    if instrumento:
        return render(request, 'app/detalhar_objeto.html', {'instrumento': instrumento})
