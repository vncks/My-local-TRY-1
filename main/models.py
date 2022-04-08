from django.db import models

class Langs(models.Model):
    title = models.CharField('Name', max_length=50)
    langs = models.TextField('lang_name')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lang'
        verbose_name_plural = 'Langs'