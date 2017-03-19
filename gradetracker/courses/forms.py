from django import forms
from django.forms import ModelForm
from courses.models import Assessment

from .models import Course

# class PostForm(forms.CourseForm):
#
#     class Meta:
#         model = Course
#         fields = ('title', 'text',)

class AssessmentForm(ModelForm):
    class Meta:
        model = Assessment
        fields = ['aname', 'apercentage', 'duedate', 'agid']

