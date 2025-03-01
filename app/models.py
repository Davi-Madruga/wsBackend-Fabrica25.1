from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    senha = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
    
class Instrument(models.Model):
    item = models.CharField(max_length=30)
    descricao = models.TextField(max_length=100)
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item
