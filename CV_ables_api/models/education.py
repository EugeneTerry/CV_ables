from django.db import models
from .applicant import Applicant
class Education(models.Model):
    applicant = models.ForeignKey(
        Applicant, models.CASCADE, related_name = "education"
        )
    school_name = models.CharField(
        max_length= 100, null = True
        )
    city = models.CharField(
        max_length= 500, null = True
        )
    state = models.CharField(
        max_length= 2, null = True
        )
    diploma = models.CharField(
        max_length= 100, null = True
        )
    grad_year = models.CharField(
        max_length= 4, null = True
        )
    def __str__(self):
        return self.school_name