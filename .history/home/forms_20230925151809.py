from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def __init__