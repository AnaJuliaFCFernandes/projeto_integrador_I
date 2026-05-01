from django.conf import settings
from django.db import models
from django.utils import timezone


# 1. Cadastro de Clientes
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=18, unique=True, verbose_name="CPF ou CNPJ")
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    endereco = models.TextField(verbose_name="Endereço")
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

# 2. Cadastro de Dispositivos (Celulares/Tablets)
class Dispositivo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dispositivos')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    imei_serial = models.CharField(max_length=50, unique=True, verbose_name="IMEI ou Serial")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.cliente.nome})"

# 3. Ordens de Serviço e Manutenção
class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('manutencao', 'Em Manutenção'),
        ('finalizada', 'Finalizada/Pronta'),
        ('entregue', 'Entregue ao Cliente'),
        ('descarte', 'Destinado ao Descarte'),
    ]

    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    defeito_relatado = models.TextField()
    laudo_tecnico = models.TextField(blank=True, null=True)
    valor_orcamento = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    data_entrada = models.DateTimeField(default=timezone.now)
    data_saida = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"OS {self.id} - {self.dispositivo.modelo}"