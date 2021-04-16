from django.db import models

# Create your models here.
class Threat(models.Model):
  email = models.TextField()
  severity = models.TextField()
  isRemediated = models.BooleanField()