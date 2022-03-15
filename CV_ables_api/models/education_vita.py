from django.db import models
from .education import Education
from .vita import Vita

class EducationVita(models.Model):
    education = models.ForeignKey(
        Education, models.CASCADE, related_name = "education_vita"
        )
    vita = models.ForeignKey(
        Vita, models.CASCADE, related_name = "education_vita"
        )