import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawly.settings')
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import commentBox, Thought, Comment, thoughtBox
from django.http import HttpResponseRedirect

def index(request):
    context = RequestContext(request)
    thought_list = Thought.objects.order_by('id')[:10]
    context_dict = {'thought_list':thought_list}
    if request.method == 'POST':
		form = thoughtBox(request.POST)
		form.save()
    else:
        form = thoughtBox()
    context_dict['form'] = form
    return render_to_response('Port/index.html', context_dict, context)

def thought(request, thought_id):
	context = RequestContext(request)
	context_dict = {'thought_id':thought_id}
	thought_id_int = int(thought_id)
	thought = Thought.objects.get(id=thought_id_int)
	child_thoughts = Thought.objects.filter(parent=thought_id_int)
	context_dict['child_thoughts'] = child_thoughts
	context_dict['thought'] = thought
	thought.comment_set.all()
	form = commentBox()
	context_dict['form'] = form
	return render_to_response('Port/thought.html', context_dict, context)

def add_comment(request, thought_id):
	thought_id_int = int(thought_id)
	thought = Thought.objects.get(id=thought_id_int)
	if request.method == 'POST':
		form = commentBox(request.POST)
		if form.is_valid():
			f = form.save(commit= False)
			f.thought = thought
			f.save()
			return HttpResponseRedirect('/port/%s/'% thought_id)

def chain(request, thought_id, comment_id):
	comment_id_int = int(comment_id)
	text = (Comment.objects.get(id = comment_id_int)).comment
	c = Thought.objects.get_or_create(thought = text, parent = int(thought_id))[0]
	new_thought_id_str = str(c.id)
	return HttpResponseRedirect('/port/%s/'% thought_id)

