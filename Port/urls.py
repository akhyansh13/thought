from django.conf.urls import patterns, include, url
from Port.views import thought, add_comment, chain, index

urlpatterns = patterns('',

	url(r'^(?P<thought_id>\w+)/$', thought),
	url(r'^(?P<thought_id>\w+)/add_comment/$', add_comment),
	url(r'^(?P<thought_id>\w+)/chain/(?P<comment_id>\w+)/$', chain),
	url(r'^$', index),
	)
