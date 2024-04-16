from django.shortcuts import render,get_object_or_404
from galeria.models import Fotografia
def index(request):
    fotos = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request,'galeria/index.html',{"cards": fotos})
def imagem(request,foto_id):
    fotos=get_object_or_404(Fotografia,pk=foto_id)
    return render(request,'galeria/imagem.html',{'fotografia':fotos}) 
def buscar(request):
    fotos=Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    
    if 'buscar' in request.GET:
        busca = request.GET['buscar'] 
        if busca:
            fotos=fotos.filter(nome__icontains=busca)

    return render(request,'galeria/buscar.html',{'cards':fotos}) 