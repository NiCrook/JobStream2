# from django.contrib.auth.models import User
# from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
# from django.urls import reverse
# from allauth.utils import get_request_param
from django.views import View
from django.urls.base import reverse

from .models import CandidateProfile, CompanyProfile
from .forms import CandidateProfileForm

from allauth.account import app_settings
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup  # passthrough_next_redirect_url
from allauth.exceptions import ImmediateHttpResponse


class CandidateSignUpView(SignupView, View):
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.user = form.save(self.request)
        self.user.is_candidate = True
        self.user.save()
        success_url = reverse('candidate_profile', kwargs={'username': self.user.username})
        try:
            return complete_signup(
                self.request,
                self.user,
                app_settings.EMAIL_VERIFICATION,
                success_url,
            )
        except ImmediateHttpResponse as e:
            return e.response


class CompanySignUpView(SignupView, View):
    success_url = 'profile/<str:username>/'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {
            'form': form,
        })

    def form_valid(self, form):
        # By assigning the User to a property on the view, we allow subclasses
        # of SignupView to access the newly created User instance
        self.user = form.save(self.request, commit=False)
        self.user.is_company = True
        self.user.save()
        try:
            return complete_signup(
                self.request,
                self.user,
                app_settings.EMAIL_VERIFICATION,
                self.success_url,
            )
        except ImmediateHttpResponse as e:
            return e.response


class CandidateProfileView(View):
    form_class = CandidateProfileForm
    template = "Profile/base_candidate_profile.html"

    def get(self, request, *args, **kwargs):
        data = {
            'full_name': CandidateProfile.full_name,
            'desired_location': CandidateProfile.desired_location,
            'desired_title': CandidateProfile.desired_title,
            'resume': CandidateProfile.resume,
            'cover_letter': CandidateProfile.cover_letter
        }
        form = self.form_class(data)
        username = request.user.username
        return render(request, self.template, {'form': form, 'username': username})
