from django.db import models

class Specialty(models.Model):
    specialty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()