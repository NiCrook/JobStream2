from django import forms


class KeywordForm(forms.Form):
    input_keywords = forms.CharField(label="Keywords", max_length='100', required=False)


class LocationForm(forms.Form):
    input_location = forms.CharField(label="Location", max_length="250", required=False)
