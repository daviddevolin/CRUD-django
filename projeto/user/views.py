from django.shortcuts import render
from .models import User

# retornando todos users para o index.html
def home(request):
    users = User.objects.all
    return render(request,"index.html",{"users":users})
# Create your views here.
