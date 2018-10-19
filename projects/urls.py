from django.conf.urls import url
from .views import SiteListView
#, SiteDetailView, SiteCreateView, SiteUpdateView,SiteDeleteView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',SiteListView.as_view(),name = 'home'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
