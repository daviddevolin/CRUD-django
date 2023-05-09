from django.shortcuts import render
from .models import User

# retornando todos users para o index.html
def home(request):
    #varrendo o objeto
    users = User.objects.all()
    return render(request,"index.html",{"users":users})
# Create your views here.

def salvar(request):
    vnome = request.POST.get("nome")
    #preenchendo o campo nome no models com o valor da variavel nome acima obtido atraves do get
    User.objects.create(nome=vnome)
    #atualizando a lista de users e enviando para
    users = User.objects.all()
    return render(request,"index.html",{"users":users})