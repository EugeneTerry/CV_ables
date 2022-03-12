from django.db import models

class Language(models.Model):
    label = models.CharField(
        max_length= 20, null = True
    )
    def __str__(self):
        return self.label