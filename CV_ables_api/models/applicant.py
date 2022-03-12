from django.db import models
from django.contrib.auth.models import User

class Applicant(models.Model):
    """yty"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="applicant")
    github_url = models.URLField(
        max_length=500 , null = True
        )
    portfolio_url = models.URLField(
        max_length=500, null = True
        )
    linkedin_url = models.URLField(
        max_length=500, null = True
        )
    address = models.CharField(
        max_length=100, null = True
        )
    city = models.CharField(
        max_length=100, null = True
        )
    state = models.CharField(
        max_length=2, null = True
        )
    zipcode = models.CharField(
        max_length=10, null = True
        )
    phone = models.CharField(
        max_length=15, null = True
        )
    
    def __str__(self):
        return self.user.first_name
    