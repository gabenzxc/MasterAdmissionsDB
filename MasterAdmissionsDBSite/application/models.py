from django.db import models

from abiturient.models import Abiturient
from specialty.models import Specialty
from exam.models import Exam
# Create your models here.
class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    abiturient = models.ForeignKey(Abiturient, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=255)
