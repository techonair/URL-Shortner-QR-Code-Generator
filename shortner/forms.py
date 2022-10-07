from django import forms
from django import forms
from . models import Shortner

class URLShortnerForm(forms.ModelForm):

    long_url = forms.URLField(
            widget=forms.URLInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Your Long URL"
                }
            )
        )

    class Meta:
        model = Shortner
        fields = ('long_url',)