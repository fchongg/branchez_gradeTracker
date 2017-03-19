from django import forms
from django.forms import ModelForm
from courses.models import Assessment, AssessmentGroup

from .models import Course

class CourseForm(ModelForm):

	class Meta:
	    model = Course
	    fields = ['cname', 'term']

class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        fields = ['aname', 'apercentage', 'duedate', 'agid']

class AssessmentGroupForm(ModelForm):
    class Meta:
        model = AssessmentGroup
        # fields = ['cid', 'agpercentage', 'agtid']
        fields = ['agpercentage', 'agtid']
