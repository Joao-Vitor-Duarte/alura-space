from django.shortcuts import render,get_object_or_404
from galeria.models import Fotografia
def index(request):
    fotos = Fotografia.objects.all()
    return render(request,'galeria/index.html',{"cards": fotos})
def imagem(request,foto_id):
    fotos=get_object_or_404(Fotografia,pk=foto_id)
    return render(request,'galeria/imagem.html',{'fotografia':fotos}) 