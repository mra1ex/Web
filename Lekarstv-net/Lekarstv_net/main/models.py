from django.db import models

# Create your models here.


class Peoples(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    mail = models.EmailField('Почта', max_length=150)
    password = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'