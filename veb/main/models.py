from django.db import models

class Task(models.Model):
    title = models.CharField("название", max_length=250)
    task = models.TextField("описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
class Bet(models.Model):
    title = models.CharField("название", max_length=250)
    body = models.TextField("описание")

    def __str__(self):
        return self.title
