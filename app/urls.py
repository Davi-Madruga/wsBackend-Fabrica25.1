from django.urls import path
from .views import *

urlpatterns = [
    path('criar/', criar_view, name='criar'),
    path('listar/', listar_view, name='listar'),
    path('editar/', editar_view, name='editar'),
    path('deletar/', deletar_view, name='deletar'),
    path('detalhar/', detalhar_view, name='detalhar'),
]
