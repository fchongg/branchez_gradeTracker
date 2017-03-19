from django import forms
from django.forms import ModelForm
from courses.models import Assessment

from .models import Course

class CourseForm(ModelForm):

	class Meta:
	    model = Course
	    fields = ['cname', 'term']

class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        fields = ['aname', 'apercentage', 'duedate', 'agid']
