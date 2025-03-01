from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('criar/', criar_view, name='criar'),
    path('listar/', listar_view, name='listar'),
    path('editar/<int:pk>', editar_view, name='editar'),
    path('deletar/<int:pk>', deletar_view, name='deletar'),
    path('detalhar/<int:pk>', detalhar_view, name='detalhar'),
]
