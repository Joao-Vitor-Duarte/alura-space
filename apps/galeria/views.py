from django.shortcuts import render,get_object_or_404,redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm
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

    return render(request,'galeria/index.html',{'cards':fotos}) 
def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request,'usuário não logado')
        return redirect('login')
    form =FotografiaForm
    if request.method == 'POST':
        form = FotografiaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success('foto cadastrada')
            return redirect('index')

    return render(request,'galeria/nova_imagem.html',{'form':form})
def editar_imagem(request,foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForm(instance=fotografia)
    
    if request.method =='POST':
        form = FotografiaForm(request.POST,request.FILES,instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request,'fotografia editada')
            return redirect('index')
    
    return render(request,'galeria/editar_imagem.html',{'form':form,'foto_id':foto_id})
    
def deletar_imagem(request,foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request,'Fotografia deletada')
    
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})