from django.urls import path
from .views import Studyplan

urlpatterns = [
    path("study-plan/", Studyplan.as_view(), name='study-plan'),
]
