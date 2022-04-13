from tabnanny import verbose
from django.db import models

from .list import List


class ListItem(models.Model):
    '''
    A classe ListItem serve para armazernar os(as) itens de lista do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo ListItem.
    '''

    name = models.CharField(
        verbose_name='Name',
        max_length=100
    )

    list = models.ForeignKey(
        List,
        verbose_name='List',
        on_delete=models.CASCADE
    )

    done = models.BooleanField(
        verbose_name='Done',
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'core'
        verbose_name = 'List item'
        verbose_name_plural = 'List items'
