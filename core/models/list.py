from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    '''
    A classe List serve para armazernar os(as) listas do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo List.
    '''

    name = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    owner = models.ForeignKey(
        User,
        verbose_name='Owner',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
