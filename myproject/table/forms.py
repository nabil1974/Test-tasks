from django import forms
from django.forms.formsets import BaseFormSet

NUMBER_OF_ROWS = 6
NUMBER_OF_CELLS = 5
MIN_LETTERS = 5
MAX_LETTERS_FROM = 10
MAX_LETTERS_TO = 15


class RowForm(forms.Form):
    cell = forms.CharField(label='Ячейка', max_length=100)


class RowFormSet(BaseFormSet):
    min_num = 0
    max_num = NUMBER_OF_CELLS
    absolute_max = NUMBER_OF_CELLS
    extra = NUMBER_OF_CELLS
    form = RowForm
    can_order = False
    can_delete = False
    validate_max = True
    validate_min = True

    def __init__(self, *args, **kwargs):
        super(RowFormSet, self).__init__(*args, **kwargs)
        for i in range(0, NUMBER_OF_CELLS):
            self[i].fields['cell'].label += " %d" % (i + 1)
