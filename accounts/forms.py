from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import UserData

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                widget = field.widget
                if type(widget) is forms.TextInput:
                    pass
                elif type(widget) is forms.Textarea:
                    pass
                widget.attrs['placeholder'] = field.label


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ("institute", "profile_picture")

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                widget = field.widget
                if type(widget) is forms.TextInput:
                    pass
                elif type(widget) is forms.Textarea:
                    pass
                widget.attrs['placeholder'] = field.label


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
