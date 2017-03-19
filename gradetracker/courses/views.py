from django.http import HttpResponse

from .models import Course
from .models import AssessmentGroup
from .models import Assessment
from django.shortcuts import render
from .Courseforms import CourseForm

def index(request):
    return HttpResponse("Hello, you're at the courses section")


def courseDetail(request):

    return HttpResponse();

def courses(request):


	return HttpResponse("courses")

def addcourses(request):


	# Create a form instance from POST data.
	f = CourseForm(request.POST)

	# Save a new Article object from the form's data.
	new_course = f.save()

	# Create a form to edit an existing Article, but use
	# POST data to populate the form.
	a = Course.objects.get(pk=1)
	f = Courseforms(request.POST, instance=a)
	f.save()
	return render(request, 'courses/addcourses.html')


