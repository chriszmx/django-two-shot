from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput,)


# feature 10 signup

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, max_length=150)
    password_confirmation = forms.CharField(widget=forms.PasswordInput,
                                            max_length=150)

    class Meta:
        fields = (
            'username',
            'password',
            'password_confirmation',
        )
