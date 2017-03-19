from django.http import HttpResponse

from .models import Course
from .models import AssessmentGroup
from .models import Assessment
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, you're at the courses section")


def courseDetail(request):

    return HttpResponse();

def courses(request):


	return HttpResponse("courses")

def addcourses(request):

    return render(request, 'courses/addcourses.html')

