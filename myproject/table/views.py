from django.urls import reverse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .models import Cell, Row
from .forms import RowFormSet, NUMBER_OF_ROWS


def index(request):
    rows = Row.objects.all()
    return render(request, 'table/index.html', {'rows': rows})


def populate_rows(request):
    if Row.objects.count() == 0:
        for i in range(NUMBER_OF_ROWS):
            row = Row.create()
    return HttpResponseRedirect(reverse('table:index'))


def purge_table(request):
    Row.objects.all().delete()
    return HttpResponseRedirect(reverse('table:index'))


def delete_row(request, row_pk):
    try:
        row = Row.objects.get(pk=row_pk)
    except Row.DoesNotExist:
        return HttpResponse('Такая строка не существует')
    row.delete()
    return HttpResponseRedirect(reverse('table:index'))


def add_row(request):
    if request.method == 'POST':
        formset = RowFormSet(request.POST)
        if formset.is_valid():
            row = Row.objects.create()
            for form in formset:
                cd = form.cleaned_data
                content = cd.get('cell')
                cell = Cell.objects.create(content=content, row=row)
            return HttpResponseRedirect(reverse('table:index'))
    else:
        formset = RowFormSet()

    return render(request, 'table/add-row.html', {'formset': formset})


def edit_row(request, row_pk):
    try:
        row = Row.objects.get(pk=row_pk)
    except Row.DoesNotExist:
        return HttpResponse('Такая строка не существует')

    cells = Cell.objects.filter(row=row)

    contents = []

    if request.method == 'POST':
        formset = RowFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                cd = form.cleaned_data
                content = cd.get('cell')

                contents.append(content)

            for i, cell in enumerate(cells):
                cell.content = contents[i]
                cell.save()
        return HttpResponseRedirect(reverse('table:index'))
    else:
        formset = RowFormSet()

    return render(request, 'table/edit-row.html', {'formset': formset, 'row_pk': row_pk})
