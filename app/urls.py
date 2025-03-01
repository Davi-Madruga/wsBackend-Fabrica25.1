from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    #Usuario
    path('criar/', criar_view, name='criar'),
    path('listar/', listar_view, name='listar'),
    path('editar/<int:pk>', editar_view, name='editar'),
    path('deletar/<int:pk>', deletar_view, name='deletar'),
    path('detalhar/<int:pk>', detalhar_view, name='detalhar'),
    #Instrument
    path('criar_objeto/', criar_objeto, name='criar_objeto'),
    path('listar_objeto/', listar_objeto, name='listar_objeto'),
    path('editar_objeto/<int:pk>', editar_objeto, name='editar_objeto'),
    path('deletar_objeto/<int:pk>', deletar_objeto, name='deletar_objeto'),
    path('detalhar_objeto/<int:pk>', detalhar_objeto, name='detalhar_objeto'),
]
