from django.forms import ModelForm
from models import Comment

class commentBox(forms.ModelForm):
	class Meta:
		model = Comment