from django.shortcuts import render
from .models import ProjectData
# Create your views here.
def home(request):
    return render(request,'home/index.html')

def projects(request):
    projectdata=ProjectData.objects.all()
    data={
        'projectdata':projectdata
    }

    

    return render(request,'projects/projects.html',data)


def contact(request):
    return render(request,'contact/contact.html')