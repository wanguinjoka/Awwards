from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class SiteCreateView(LoginRequiredMixin, CreateView):
    model = Site
    fields = ['title','site_image','description','site_url']

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)

class SiteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Site
    fields = ['title','site_image','description','site_url']

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        site = self.get_object()
        if self.request.user == site.developer:
            return True
        return False

class SiteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Site
    success_url = '/'

    def test_func(self):
        site = self.get_object()
        if self.request.user == site.developer:
            return True
        return False

def search_results(request):

    if 'site' in request.GET and request.GET["site"]:
        search_term = request.GET.get("site")
        searched_sites = Site.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html',{"message":message,"sites": searched_sites})

    else:
        message = "You haven't searched for any term"
        return render(request, 'projects/search.html',{"message":message})
