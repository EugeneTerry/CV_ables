from django.db import models

class Language(models.Model):
    lable = models.CharField(
        max_length= 20, null = True
    )