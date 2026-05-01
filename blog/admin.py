from django.contrib import admin
from .models import Cliente, Dispositivo, OrdemServico

admin.site.register(Cliente)
admin.site.register(Dispositivo)
admin.site.register(OrdemServico)