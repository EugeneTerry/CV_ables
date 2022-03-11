from django.db import models

class Jobtype(models.Model):
    label = models.CharField(
        max_length= 25, null = True
    )
    def __str__(self):
        return self.label