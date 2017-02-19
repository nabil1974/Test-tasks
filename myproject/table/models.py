from django.db import models
import random
import string

from .forms import NUMBER_OF_CELLS, MIN_LETTERS, MAX_LETTERS_FROM, MAX_LETTERS_TO


class Cell(models.Model):
    content = models.CharField(max_length=100, null=True, blank=True)
    row = models.ForeignKey('Row')

    def __str__(self):
        try:
            return '{}'.format(self.content[:10])
        except TypeError:
            return ''


class Row(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls):
        row = cls()
        row.save()
        for i in range(NUMBER_OF_CELLS):
            content = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(MIN_LETTERS, random.randint(MAX_LETTERS_FROM, MAX_LETTERS_TO)))
            cell = Cell.objects.create(content=content, row=row)
        return row

    class Meta:
        ordering = ('-created',)

    # def __str__(self):
    #     return '{}'.format(self.pk)
