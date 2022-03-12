from django.db import models
from .applicant import Applicant
class Prospect(models.Model):
    applicant = models.ForeignKey(
        Applicant, models.CASCADE, related_name = "prospect"
        )
    prospect_name = models.CharField(
        max_length= 100, null = True
        )
    listing_url = models.URLField(
        max_length=500, null = True
        )
    def __str__(self):
        return self.prospect_name