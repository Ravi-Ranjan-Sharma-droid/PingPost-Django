from django import forms
from .models import Tweet  #  Corrected import

class TweetForm(forms.ModelForm):  #  Correct base class
    class Meta:
        model = Tweet             #  Tell Django which model this form is for
        fields = ['text', 'photo']
