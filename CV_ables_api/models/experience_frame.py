from django.db import models
from .applicant import Applicant
from .experience import Experience
from .framework import Framework
from .project import Project

class ExperienceFrame(models.Model):
    applicant = models.ForeignKey(
        Applicant, models.CASCADE, related_name = "experience_frame"
        )
    experience = models.ForeignKey(
        Experience, models.CASCADE, related_name = "experience_frame"
        )
    framework = models.ForeignKey(
        Framework, models.CASCADE, related_name = "experience_frame"
        )
    project = models.ForeignKey(
        Project, models.CASCADE, related_name = "experience_frame"
        )