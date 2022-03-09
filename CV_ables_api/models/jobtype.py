from django.db import models

class Jobtype(models.Model):
    lable = models.CharField(
        max_length= 25, null = True
    )
    