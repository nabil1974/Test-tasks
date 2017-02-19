from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^populate-rows/$', views.populate_rows, name='populate_rows'),
    url(r'^purge-table/$', views.purge_table, name='purge_table'),
    url(r'^delete-row/(?P<row_pk>[0-9]+)/$', views.delete_row, name='delete_row'),
    url(r'^add-row/$', views.add_row, name='add_row'),
    url(r'^(?P<row_pk>[0-9]+)/$', views.edit_row, name='edit_row')
]
