from django.db import models
from .jobtype import Jobtype
from .applicant import Applicant
class Mission (models.Model):
    mission_text = models.CharField(
        max_length= 500, null = True
    )
    applicant = models.ForeignKey(
        Applicant, models.CASCADE,
        related_name = "mission"
    )
    job_type = models.ForeignKey(
        Jobtype, models.CASCADE,
        related_name = "mission"
    )
    def __str__(self):
        return self.job_type.label