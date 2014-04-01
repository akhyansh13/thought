from django.db import models
from django import forms

class Thought(models.Model):
	thought = models.CharField(max_length=10000000)

class Comment(models.Model):
	thought = models.ForeignKey(Thought)
	comment = models.CharField(max_length=10000000)
	
class commentBox(forms.ModelForm):
	comment = forms.CharField(max_length=10000000,widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
	class Meta:
		model = Comment
		fields = ('comment',)
		
		
		