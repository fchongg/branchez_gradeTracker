from django import forms
from django.forms import ModelForm
from courses.models import Assessment

from .models import Course

TERM_CHOICES = (
    ('W1', 'W2', 'S1', 'S2'),
    )

class CourseForm(forms.Form):
	add_cname = forms.CharField(label='add_cname', max_length=100)
	add_term = forms.CharField(
		label = 'add_term',
        max_length=2,
        widget=forms.Select(choices=TERM_CHOICES),
        )

class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        fields = ['aname', 'apercentage', 'duedate', 'agid']