from django.db import models
from .applicant import Applicant
from .prospectstatus import ProspectStatus
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
    markedvita = models.CharField(
        max_length= 100, null = True
        )
    prospectstatus = models.ForeignKey(
        ProspectStatus, models.CASCADE, null = True, related_name = "prospect"
        )    
    notes = models.CharField(
        max_length= 2000, null = True
        )
    def __str__(self):
        return self.prospect_name