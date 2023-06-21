from django.db import models

# Create your models here.


class People(models.Model):
    mail = models.EmailField('Почта', max_length=150)
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    password = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Like(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
