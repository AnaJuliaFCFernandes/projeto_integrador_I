from django.contrib import admin
from .models import Post, Cliente, Dispositivo, OrdemServico

admin.site.register(Post)
admin.site.register(Cliente)
admin.site.register(Dispositivo)
admin.site.register(OrdemServico)