from django.db import models
from django.urls import reverse

# Create your models here.
class Application(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key=True)
    education = models.CharField(max_length=100)
    college_name = models.CharField(max_length=150)
    passing_year = models.CharField(max_length=10)
    about = models.CharField(max_length=500)
    notes = models.CharField(max_length=250, blank=True, null=True)
    dob = models.DateField()
    application_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default='download.png')
    resume = models.FileField(upload_to='docs/', blank=True, null=True)
