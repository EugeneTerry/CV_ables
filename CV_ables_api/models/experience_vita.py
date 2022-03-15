from django.db import models
from .experience import Experience
from .vita import Vita

class ExperienceVita(models.Model):
    experience = models.ForeignKey(
        Experience, models.CASCADE, related_name = "experience_vita"
        )
    vita = models.ForeignKey(
        Vita, models.CASCADE, related_name = "experience_vita"
        )