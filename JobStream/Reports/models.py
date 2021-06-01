from django.contrib.auth.models import User
from django.db import models


class CandidateReport(models.Model):
    CHOOSE = 'CHOOSE'
    SPAM = 'SPAM'
    DANGEROUS = 'DANGEROUS'
    ILLEGAL = 'ILLEGAL'

    CANDIDATE_CATEGORY_CHOICES = (
        (CHOOSE, 'Choose'),
        (SPAM, 'Spam'),
        (DANGEROUS, 'Dangerous'),
        (ILLEGAL, 'Illegal'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    # article = models.ForeignKey()  TODO fix this
    category = models.CharField(
        max_length=10,
        choices=CANDIDATE_CATEGORY_CHOICES,
        default=CHOOSE,
    )
    comment = models.TextField(blank=True)


class CompanyReport(models.Model):
    CHOOSE = 'CHOOSE'
    SPAM = 'SPAM'
    DANGEROUS = 'DANGEROUS'
    ILLEGAL = 'ILLEGAL'

    COMPANY_CATEGORY_CHOICES = (
        (CHOOSE, 'Choose'),
        (SPAM, 'Spam'),
        (DANGEROUS, 'Dangerous'),
        (ILLEGAL, 'Illegal'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=10,
        choices=COMPANY_CATEGORY_CHOICES,
        default=CHOOSE
    )
    comment = models.TextField(blank=True)