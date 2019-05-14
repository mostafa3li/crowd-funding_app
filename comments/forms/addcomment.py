from django import forms
from projects.models import *
from comments.models import *
from users.models import *
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title']
   
  