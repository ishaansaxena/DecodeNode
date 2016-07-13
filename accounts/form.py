from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(_('first name'), max_length=30, blank=True)
    last_name = forms.CharField(_('last name'), max_length=30, blank=True)
    profile_picture = forms.ImageField(upload_to='static/assets/user_images/', blank=True)
