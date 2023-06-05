from django.db import models

class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()