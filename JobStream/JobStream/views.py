from django.shortcuts import render
from django.views import View

from .forms import KeywordForm, LocationForm

from allauth import app_settings
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse


def home_view(request):
    keyword_form = KeywordForm()
    location_form = LocationForm()

    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'base.html', {
            'keyword_form': keyword_form,
            'location_form': location_form,
            'username': username
        })
    else:
        return render(request, 'base.html', {
            'keyword_form': keyword_form,
            'location_form': location_form
        })


def about(request):
    return render(request, 'about.html')


# class CandidateSignUpView(SignupView, View):
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def form_valid(self, form):
#         # By assigning the User to a property on the view, we allow subclasses
#         # of SignupView to access the newly created User instance
#         self.user = form.save(self.request, commit=False)
#         self.user.is_candidate = True
#         self.user.save()
#         try:
#             return complete_signup(
#                 self.request,
#                 self.user,
#                 app_settings.EMAIL_VERIFICATION,
#                 self.get_success_url(),
#             )
#         except ImmediateHttpResponse as e:
#             return e.response
#
#
# class CompanySignUpView(SignupView, View):
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
