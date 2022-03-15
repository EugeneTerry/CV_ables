from django.db import models
from .jobtype import Jobtype
from .applicant import Applicant
class Mission (models.Model):
    mission_text = models.CharField(
        max_length= 500, null = True
    )
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE,
        related_name = "missions"
    )
    job_type = models.ForeignKey(
        Jobtype, on_delete=models.CASCADE,
        related_name = "missions"
    )
    def __str__(self):
        return self.jobtype.label