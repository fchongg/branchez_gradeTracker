from django import forms

from .models import Course

class PostForm(forms.CourseForm):

    class Meta:
        model = Course
        fields = ('title', 'text',)