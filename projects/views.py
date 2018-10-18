from django.shortcuts import render
from .models import Site

# Create your views here.
def home(request):
    context= {
         'sites': Site.objects.all()
         }
    return render(request,'projects/home.html', context)
