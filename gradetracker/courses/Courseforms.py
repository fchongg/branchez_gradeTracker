from django import forms

TERM_CHOICES = (
    ('W1', 'W2', 'S1', 'S2'),
    )

class CourseForm(forms.forms):
	coursename = forms.CharField(max_length = 100)
	term = forms.CharField(
        max_length=2,
        widget=forms.Select(choices=TERM_CHOICES),
    )
