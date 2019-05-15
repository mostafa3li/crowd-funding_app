from django import forms
import datetime

from .models import Category, Project

class AddProjectForm(forms.Form):
  title = forms.CharField(label='Title',max_length=120,widget=forms.TextInput(attrs={
    "placeholder": "Project title"
  }))
  details = forms.CharField(label='Details',widget=forms.TextInput(attrs={
    "placeholder": "Project Details"
  }))
  # CATEGORIES = ()
  # for category in Category.objects.all():
  #   CATEGORIES = CATEGORIES + ((category.id, category.title),)
  # category = forms.ChoiceField(choices=CATEGORIES)
  category = forms.ModelChoiceField(queryset=Category.objects.all())
  # category = forms.CharField(label="test",widget=forms.Select(choices=CATEGORIES))
  target = forms.IntegerField(initial=0, min_value=0)
  start_date = forms.DateField(label='start date',initial=datetime.date.today)
  end_date = forms.DateField(label='end date',initial=datetime.date.today)


# //! model form
class ProjectModelForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = [
      'title',
      'details',
      'category',
      'target',
      # 'start_date',
      'end_date',
    ]