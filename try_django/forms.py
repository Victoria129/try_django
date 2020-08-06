from django import forms
from django.forms import Textarea


class ContactForm(forms.Form):
    full_name  = forms.CharField()
    email      = forms.EmailField()
    content    = forms.CharField(widget=Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.validationError("This is not a valid email. Please don't use .edu.")
        return email
