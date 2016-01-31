from django.conf.urls import url
from django.contrib import admin

from .views import (
	ahs_list,
	ahs_create,
	ahs_detail,
	ahs_update,
	ahs_delete,
	)

urlpatterns = [
	url(r'^$', ahs_list, name='list'),
    url(r'^create/$', ahs_create),
    url(r'^detail/(?P<id>\d+)$', ahs_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ahs_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', ahs_delete),
    #url(r'^ahss/$', "<appname>.views.<function_name>"),
]