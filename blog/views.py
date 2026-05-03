from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import OrdemServico, Cliente, Dispositivo # Importe seus novos modelos
from .forms import OrdemServicoForm
from django.db.models import Q


def post_list(request):
    query = request.GET.get('search')
    if query:
        # Filtra se o nome do cliente contém a busca OU se o modelo do dispositivo contém a busca
        ordens = OrdemServico.objects.filter(
            Q(dispositivo__cliente__nome__icontains=query) | 
            Q(dispositivo__modelo__icontains=query) |
            Q(id__icontains=query)
        ).order_by('-data_entrada')
    else:
        ordens = OrdemServico.objects.all().order_by('-data_entrada')
        
    return render(request, 'blog/post_list.html', {'ordens': ordens})

# Detalhes de uma Ordem de Serviço específica
def os_detail(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    return render(request, 'blog/os_detail.html', {'ordem': ordem})

# Criar nova Ordem de Serviço
def os_nova(request):
    if request.method == "POST":
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            os = form.save(commit=False)
            # Se quiser registrar quem criou, pode usar os.tecnico = request.user
            os.save()
            return redirect('os_detail', pk=os.pk)
    else:
        form = OrdemServicoForm()
    return render(request, 'blog/os_edit.html', {'form': form})

# Editar uma Ordem de Serviço existente
def os_edit(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == "POST":
        form = OrdemServicoForm(request.POST, instance=ordem)
        if form.is_valid():
            os = form.save(commit=False)
            os.save()
            return redirect('os_detail', pk=os.pk)
    else:
        form = OrdemServicoForm(instance=ordem)
    return render(request, 'blog/os_edit.html', {'form': form})