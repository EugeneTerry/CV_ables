from django.db import models
from .experience import Experience 
class Description(models.Model):
    description_text = models.CharField(
        max_length=1000, null = True
        )
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, related_name = "descriptions"
        )
    def __str__(self):
        return self.experience