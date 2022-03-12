from django.db import models
from .applicant import Applicant
from .jobtype import Jobtype
from .framework import Framework

class Experience(models.Model):
    applicant = models.ForeignKey(
        Applicant, models.CASCADE, related_name = "experience"
        )
    job_type = models.ForeignKey(
        Jobtype, models.CASCADE, related_name = "experience"
        )
    job_title = models.CharField(
        max_length= 100, null = True
        )
    company = models.CharField(
        max_length= 100, null = True
        )
    start_yr = models.CharField(
        max_length= 4, null = True
        )
    end_yr = models.CharField(
        max_length= 25, null = True
        )