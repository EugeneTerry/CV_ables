from turtle import title
from django.db import models

class Project(models.Model):
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