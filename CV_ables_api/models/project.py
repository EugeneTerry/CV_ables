from django.db import models
from .applicant import Applicant

class Project(models.Model):
    applicant = models.ForeignKey(
        Applicant, models.CASCADE, null = True, related_name = "project"
        )
    title = models.CharField(
        max_length= 25, null = True
        )
    github_url = models.URLField(
        max_length=500 , null = True
        )
    deploy_url = models.URLField(
        max_length=500 , null = True
        )
    image_url = models.URLField(
        max_length=500 , null = True
        )
    def __str__(self):
        return self.title