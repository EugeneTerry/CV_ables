from django.db import models
from .applicant import Applicant
from .jobtype import Jobtype
from .prospect import Prospect
from .mission import Mission
class Vita(models.Model):
    applicant = models.ForeignKey(
        Applicant, models.CASCADE, related_name = "vita"
        )
    job_type = models.ForeignKey(
        Jobtype, models.CASCADE, related_name = "vita"
        )
    mission = models.ForeignKey(
        Mission, models.CASCADE, related_name = "vita"
        )
    prospect = models.ForeignKey(
        Prospect, models.CASCADE, related_name = "vita"
        )
    published = models.BooleanField(
        default = False
        )
    slug = models.SlugField(
        max_length= 50, null = True
        )
    
    