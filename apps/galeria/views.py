from django.shortcuts import render,get_object_or_404,redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
def index(request):
    if not request.user.is_authenticated:
        messages.error(request,'usuário não logado')
        return redirect('login')
    fotos = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request,'galeria/index.html',{"cards": fotos})
def imagem(request,foto_id):
    
    fotos=get_object_or_404(Fotografia,pk=foto_id)
    return render(request,'galeria/imagem.html',{'fotografia':fotos}) 
def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,'usuário não logado')
        return redirect('login')
    
    fotos=Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    
    if 'buscar' in request.GET:
        busca = request.GET['buscar'] 
        if busca:
            fotos=fotos.filter(nome__icontains=busca)

    return render(request,'galeria/buscar.html',{'cards':fotos}) 
