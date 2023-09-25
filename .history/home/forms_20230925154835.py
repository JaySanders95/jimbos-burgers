from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(required=True)

    def clean_password1(self):
        cleaned_data = super().clean()
        password

        #Check password contains at least one number
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('Password must contain at least one number')
        
        #Check password contains at least one capital letter
        if not any(char.isupper() for char in password):
            raise forms.ValidationError('Password must contain at least one capital letter')
        
        #Check password is 8 or more characters
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        

        return password