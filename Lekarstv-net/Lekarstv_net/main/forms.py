from .models import Peoples
from django.forms import ModelForm, TextInput, EmailInput


class PeoplesForm(ModelForm):
    class Meta:
        model = Peoples
        fields = ['name', 'surname', 'mail', 'password']

        widgets = {
            "name": TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "mail": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })


        }