from django.contrib import admin
from django.urls import path
from rest_framework import routers
from abiturient.views import AbiturientViewSet
from specialty.views import SpecialtyViewSet
from exam.views import ExamViewSet
from application.views import ApplicationViewSet
from examresult.views import ExamResultViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'abiturients', AbiturientViewSet)
router.register(r'specialties', SpecialtyViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'exam-results', ExamResultViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
