from allauth.account.forms import SignupForm
class MyCustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

from django import forms
class MyCustomSignupForm(forms.Form):    
        def __init__(self, *args, **kwargs):
                super(MyCustomSignupForm, self).__init__(*args, **kwargs)
                self.fields['First Name'] = forms.CharField(required=True)   
                self.fields['Last Name'] = forms.CharField(required=True)  
                self.fields['user_email'].widget = forms.TextInput(attrs={'type':'email','class':"form-control p-3 my-input"})
                self.fields['password'].widget = forms.PasswordInput(attrs={'type':'password','class':"form-control p-3 my-input"}) 
        def save(self, request):
                first_name = self.cleaned_data.pop('First Name')
                last_name = self.cleaned_data.pop('Last Name')
                user_email= self.cleaned_data.pop('user_email')
                password = self.cleaned_data.pop('password')
                password = self.cleaned_data.pop('password')
                user = super(MyCustomSignupForm, self).save(request)


class CustomSignupForm(forms.Form):
    opt_in = forms.BooleanField(label="Add me to the email list", help_text="Don't worry. We won't spam you.", initial=True, required=False)

    def signup(self, request, user):
        user.opt_in = self.cleaned_data['opt_in']
        user.save