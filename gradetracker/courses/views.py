from django.http import HttpResponse

from .models import Course
from .models import AssessmentGroup
from .models import Assessment
from django.template import loader
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, you're at the courses section")


def courseDetail(request):

    return HttpResponse();

def courses(request):

	current_user = request.user
	# template = loader.get_template('course')
	all_courses = Course.objects.filter(uid=1)

	context = {
       	'all_courses': all_courses,
   	}
	return render(request, 'courses/course.html', context)

def addcourses(request):

    return render(request, 'courses/addcourses.html')

