from django.shortcuts import render

def criar_view(request):
    return render(request, 'criar.html')

def listar_view(request):
    return render(request, 'listar.html')

def editar_view(request):
    return render(request, 'editar.html')

def deletar_view(request):
    return render(request, 'deletar.html')

def detalhar_view(request):
    return render(request, 'detalhar.html')
