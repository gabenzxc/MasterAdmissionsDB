from django.db import models
from application.models import Application
from exam.models import Exam
class ExamResult(models.Model):
    exam_result_id = models.AutoField(primary_key=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField()