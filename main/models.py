from django.db import models


class Notes(models.Model):
    title = models.CharField('note_name', max_length=50)
    notes = models.TextField('note')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
