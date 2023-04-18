from django.shortcuts import render
from .models import *

# Create your views here.
def team(request):
    personnes = Personne.objects.all()
    return render(request,'team.html',{'personnes':personnes})
