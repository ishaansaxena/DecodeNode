from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ProfileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    profile_picture = forms.ImageField()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                widget = field.widget
                if type(widget) is forms.TextInput:
                    # something
                    pass
                elif type(widget) is forms.Textarea:
                    # widget.attrs['class'] = 'form-control'
                    pass
                widget.attrs['placeholder'] = field.label


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    # institute = forms.CharField(label='Institute')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                widget = field.widget
                if type(widget) is forms.TextInput:
                    # something
                    pass
                elif type(widget) is forms.Textarea:
                    # widget.attrs['class'] = 'form-control'
                    pass
                widget.attrs['placeholder'] = field.label
