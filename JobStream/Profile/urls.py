from django.urls import path

from . import views

urlpatterns = [
    path('candidate-signup/', views.CandidateSignUpView.as_view(), name='candidate_signup'),
    path('company-signup/', views.CompanySignUpView.as_view(), name='company_signup'),
    path('profile/<str:username>/', views.CandidateProfileView.as_view(), name='candidate_profile'),
]
