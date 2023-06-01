"""
URL configuration for MasterAdmissionsDBSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
