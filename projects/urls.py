from django.conf.urls import url
from .views import SiteListView, SiteDetailView, SiteCreateView, SiteUpdateView,SiteDeleteView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',SiteListView.as_view(),name = 'home'),
    url(r'^site/(?P<pk>[0-9]+)/$', SiteDetailView.as_view(), name='site-detail'),
    url(r'^site/new/', SiteCreateView.as_view(), name='site-create'),
    url(r'^site/(?P<pk>[0-9]+)/update/$', SiteUpdateView.as_view(), name='site-update'),
    url(r'^site/(?P<pk>[0-9]+)/delete/$', SiteDeleteView.as_view(), name='site-delete'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
