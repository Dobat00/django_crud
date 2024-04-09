from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud.models import Pessoa

# Create your views here.
def clearall(request):
    Pessoa.objects.all().delete()
    return render(request, 'index.html')

def index(request):
    pessoas = Pessoa.objects.all() 
    context = {"pessoas":pessoas}
    return render(request, 'index.html', context)

def salvar(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    Pessoa.objects.create(nome=nome, idade=idade)
    pessoas= Pessoa.objects.all()
    context= {"pessoas":pessoas}
    return render(request, 'index.html', context)

def editar(request, id):
    pessoa = Pessoa.objects.get(id = id)
    context = {'pessoa':pessoa}
    return render(request, 'update.html',context)

def editarPOST(request,id):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    pessoa = Pessoa.objects.get(id = id)
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.save();
    return redirect(index)

def delete(request, id):
    Pessoa.objects.get(id = id).delete()
    return redirect(index)
