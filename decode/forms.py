from django import forms


class GameForm(forms.Form):
    user_answer = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Answer'
            }
        )
    )

