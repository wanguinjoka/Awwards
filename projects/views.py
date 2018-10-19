from django.shortcuts import render
from django.views.generic import ListView,DetailView
#,CreateView,UpdateView, DeleteView
from .models import Site

# Create your views here.
def home(request):
    context= {
         'sites': Site.objects.all()
         }
    return render(request,'projects/home.html', context)

class SiteListView(ListView):
    model = Site
    template_name = 'projects/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'sites'
    ordering = ['-date_posted']

class SiteDetailView(DetailView):
    model = Site
