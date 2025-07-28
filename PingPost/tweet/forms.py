from django import forms
from .models import Tweets

class TweetForm(forms):
    class Meta:
        fields = ['text', 'photo']
