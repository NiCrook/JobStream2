from django.urls import path

from . import views

urlpatterns = [
    path('', views.CandidateReportView.as_view(), name='candidate-report'),
    path('submit_candidate_report', views.CandidateReportView.as_view(), name='report')
]
