from django import forms
from .models import Usuario, Instrument

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'data_nascimento', 'cpf', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'senha': 'Senha',
            'data_nascimento': 'Data de Nascimento',
            'cpf': 'CPF',
            'telefone': 'Telefone',
        }
        
class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['item', 'descricao', 'dono']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'dono': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'item': 'Item',
            'descricao': 'Descrição',
            'dono': 'Dono'
        }
