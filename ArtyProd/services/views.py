from django.shortcuts import render
from .models import *
# Create your views here.
def services(request):
    services = Service.objects.all()
    return render(request,'services.html',{'services' : services})