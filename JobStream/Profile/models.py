from django.contrib.auth.models import User
from django.db import models


class CandidateProfile(models.Model):
    candidate_username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=50, blank=True)
    desired_location = models.CharField(max_length=300, blank=True)
    desired_title = models.CharField(max_length=300, blank=True)
    resume = models.FileField(blank=True)
    cover_letter = models.FileField(blank=True)


class CompanyProfile(models.Model):
    company_username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=300, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    public_email = models.EmailField(blank=True)
    website = models.CharField(max_length=250, blank=True)
