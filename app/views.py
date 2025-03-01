from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

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
            return redirect('app:listar')
        
    return render(request, 'editar.html')

def deletar_view(request):
    return render(request, 'deletar.html')

def detalhar_view(request):
    return render(request, 'detalhar.html')
