from django import forms

from .models import CandidateProfile, CompanyProfile


class CandidateProfileForm(forms.Form):
    desired_location = forms.CharField(max_length=250)
    desired_title = forms.CharField(max_length=250)
    resume = forms.FileField()
    cover_letter = forms.FileField()
