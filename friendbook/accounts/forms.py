from  django import forms
from .models import Users
class Userform(forms.ModelForm):
    class Meta:
        model = Users
        fields =('username','password','email','mobile')

    username =forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',

            }
        )
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    mobile = forms.CharField(
        label='',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
