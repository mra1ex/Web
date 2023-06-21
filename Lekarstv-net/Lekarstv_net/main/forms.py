from .models import People, Like
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class PeopleForm(ModelForm):
    class Meta:
        model = People

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
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })


        }


class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = []
