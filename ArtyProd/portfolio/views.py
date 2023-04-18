from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    return render(request,'portfolio.html',{'projects':projects})


@login_required(login_url='login')
def project(request,pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project.html',{'project':project})


@login_required(login_url='login')
def req_project(request):
    if request.method == 'POST':
        libelle = request.POST.get('name')
        types = request.POST.getlist('project_type')
        description = request.POST.get('project_description')
        image = request.FILES.get('project_image')
        details = request.FILES.get('project_file')
        project = Project.objects.create(libelle=libelle, description=description, image=image ,details=details)
        project.type.set(types)

    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'req_project.html', context)