from django import forms


class JobArticleForm(forms.Form):
    position_title = forms.CharField(label='PositionTitle', max_length=250)
    location = forms.CharField(label='Location', max_length=250)  # TODO change to smarter search
    summary = forms.CharField(label='Summary', max_length=500)
    description = forms.CharField(label='Description', max_length=3000)
    requirements = forms.CharField(label='Requirements', max_length=3000)
    benefits = forms.CharField(label='Benefits', max_length=3000)
    others = forms.BooleanField()
    other = forms.CharField(label='Other', max_length=3000)
