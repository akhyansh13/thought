from django.db import models
from django import forms

class Thought(models.Model):
	thought = models.CharField(max_length=10000000)
	parent = models.IntegerField(null = True, blank = True)

class Comment(models.Model):
	thought = models.ForeignKey(Thought)
	comment = models.CharField(max_length=10000000)

class commentBox(forms.ModelForm):
	comment = forms.CharField(max_length=10000000,widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
	class Meta:
		model = Comment
		fields = ('comment',)

class thoughtBox(forms.ModelForm):
    thought = forms.CharField(max_length=10000000,widget=forms.Textarea(attrs={'rows': 8, 'cols': 80}))
    class Meta:
		model = Thought
		fields = ('thought',)

