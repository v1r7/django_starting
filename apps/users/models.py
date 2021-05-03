from django.db import models

class User(models.Models):
    first_name = models.CharField(max_lenght=255)
    last_name = models.CharField(max_lenght=255)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def ___str___(self):
        return f'{self.last_name.capitalize} {self.first_name.capitalize}'
