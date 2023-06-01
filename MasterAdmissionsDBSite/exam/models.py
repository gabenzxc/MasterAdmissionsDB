from django.db import models

# Create your models here.
class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()