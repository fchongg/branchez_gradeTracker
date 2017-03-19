from django.http import HttpResponse

from .models import Course
from .models import AssessmentGroup
from .models import Assessment, AgType
from django.template import loader
from django.shortcuts import render
from itertools import chain
from .Courseforms import CourseForm


def index(request):
    return HttpResponse("Hello, you're at the courses section")

def courseDetail(request, course_id):
	assignmentgroups = AssessmentGroup.objects.filter(cid = course_id)
	courseName = Course.objects.get(id = course_id).cname
	assignments = []
	groupedAssignments = []
	for ag in assignmentgroups:
		assignGroupObj = {}
		t = AgType.objects.get(id=ag.agtid.id).agname
		assignGroupObj[t] = list(Assessment.objects.filter(agid = ag.id).order_by('-duedate'))
		groupedAssignments.append(assignGroupObj)
		assignments = assignments + list(Assessment.objects.filter(agid = ag.id))
	context = {
		'assignments' : assignments,
		'courseName': courseName
	}
	return render(request, 'courses/coursedetails.html',context)

def courses(request):

	current_user = request.user
	# template = loader.get_template('course')
	all_courses = Course.objects.filter(uid=1)

	context = {
       	'all_courses': all_courses,
   	}
	return render(request, 'courses/course.html', context)

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



