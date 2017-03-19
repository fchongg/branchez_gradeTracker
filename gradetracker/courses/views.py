from django.http import HttpResponse, HttpResponseRedirect
from .models import Course
from .models import AssessmentGroup
from .models import Assessment, AgType
from django.template import loader
from django.shortcuts import render
from .forms import CourseForm
from itertools import chain
from django.views.decorators.csrf import csrf_exempt
from .forms import AssessmentForm

@csrf_exempt

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
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/courses/')
	else:
		form = CourseForm()
	return render(request, 'courses/addcourse.html', {'form' : form})

def addAssessment(request):
	if request.method == 'POST':
		form = AssessmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/courses/')
	else:
		form = AssessmentForm()

	return render(request, 'courses/addassessment.html', {'form' : form})



