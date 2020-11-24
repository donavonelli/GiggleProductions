from django import forms
from .models import Newsletter

class NewsletterSignUpForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['first_name', 'email']

        def clean_email(self): 
            email = self.cleaned_data.get('email')

            return email

        def clean_name(self):
            first_name = self.cleaned_data.get('first_name')

            return first_name