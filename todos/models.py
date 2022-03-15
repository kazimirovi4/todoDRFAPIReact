from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.title
