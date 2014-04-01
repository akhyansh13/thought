from django.conf.urls import patterns, include, url
from Port.views import index, add_comment, chain

urlpatterns = patterns('',
 
	url(r'^(?P<thought_id>\w+)/$', index),
	url(r'^(?P<thought_id>\w+)/add_comment/$', add_comment),
	url(r'^(?P<thought_id>\w+)/chain/(?P<comment_id>\w+)/$', chain),
	)
