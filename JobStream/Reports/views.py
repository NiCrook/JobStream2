from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from .forms import CandidateReportForm, CompanyReportForm
from .models import CandidateReport, CompanyReport

from datetime import datetime


class CandidateReportView(View):
    form_class = CandidateReportForm
    form_template = 'Reports/candidate_report.html'
    form_submit_template = 'Reports/report_submitted.html'
    form_submit_error = 'Reports/report_error.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.form_template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            author = User.objects.get(username='nicholas')
            category = form.cleaned_data['category']
            comment = form.cleaned_data['comment']
            new_report = CandidateReport(author=author, category=category, comment=comment)
            new_report.save()
            return render(request, self.form_submit_template)
        else:
            print(f"form.errors = {form.errors}")
            return render(request, self.form_submit_error)
