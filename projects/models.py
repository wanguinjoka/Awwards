from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Site(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    site_image = models.ImageField(upload_to='projects/')
    date_posted = models.DateTimeField(default=timezone.now)
    site_url = models.CharField(max_length=100, blank=True)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
