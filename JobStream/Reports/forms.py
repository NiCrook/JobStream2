from django import forms

from .models import CandidateReport


class CandidateReportForm(forms.Form):
    category = forms.ChoiceField(choices=CandidateReport.CANDIDATE_CATEGORY_CHOICES, label='Category')
    comment = forms.CharField(label='Comment', max_length=1000, widget=forms.Textarea)


class CompanyReportForm(forms.Form):
    category = forms.CharField(label='Category', max_length=10)
    comment = forms.CharField(label='Comment', max_length=1000, widget=forms.Textarea)
