from django.db import models
from .applicant import Applicant
from .experience import Experience
from .language import Language
from .project import Project

class ExperienceLang(models.Model):
    applicant = models.ForeignKey(
        Applicant, models.CASCADE, related_name = "experience_lang"
        )
    experience = models.ForeignKey(
        Experience, models.CASCADE, related_name = "experience_lang"
        )
    language = models.ForeignKey(
        Language, models.CASCADE, related_name = "experience_lang"
        )
    project = models.ForeignKey(
        Project, models.CASCADE, related_name = "experience_lang"
        )