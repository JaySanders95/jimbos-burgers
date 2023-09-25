from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(required=True)

    def clean_strong_password(self):
        password1 = self.cleaned_data.get('password1')

        #Check password contains at least one number
        if not any(char.isdigit() for char in password1):
            