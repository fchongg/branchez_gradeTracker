from django.http import HttpResponse, HttpResponseRedirect
from .models import Course
from .models import AssessmentGroup
from .models import Assessment, AgType
from django.template import loader
from django.shortcuts import render
from .forms import CourseForm
from itertools import chain
from django.views.decorators.csrf import csrf_exempt
from .forms import AssessmentForm, AssessmentGroupForm

import datetime
from django.utils import timezone

from django.http import QueryDict


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

	all_courses = Course.objects.filter(uid=request.user.id)
	
	context = {
       	'all_courses': all_courses,
   	}
	return render(request, 'courses/course.html', context)

def addcourses(request):
	if request.method == 'POST':
		form = CourseForm(request.POST)
		user = request.user
		if form.is_valid():
			portfolio = form.save(commit=False)
			portfolio.uid = request.user
			form.save()
			return HttpResponseRedirect('/courses/courses/')
	else:
		form = CourseForm()
	return render(request, 'courses/addcourse.html', {'form' : form})

def addAssessment(request):
	if request.method == 'POST':
		form = AssessmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/courses/courses/')
	else:
		form = AssessmentForm()

	return render(request, 'courses/addassessment.html', {'form' : form})

def addAssessmentGroup(request):
	if request.method == 'POST':
		form = AssessmentGroupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('courses/courses')
	else:
		form = AssessmentGroupForm()

	return render(request, 'courses/addgroup.html', {'form' : form})

def dashboard(request):
	# todo : get userid and input into fn
	allCourses = Course.objects.filter(uid=request.user.id)
	allAssignmentsfive = []
	percentage = 0
	priority = None
	for course in allCourses:
		assessmentGroup = AssessmentGroup.objects.filter(cid = course.id)
		for ag in assessmentGroup:
			grouppercentage = ag.agpercentage
			fiveassignment = list(Assessment.objects.filter(agid = ag.id).
										   filter(date__lt=timezone.now() - datetime.timedelta(days=5)))
			for i in range(1, len(fiveassignment) - 1):
				if priority is None:
					priority = fiveassignment[i]
					percentage = fiveassignment[i] * grouppercentage
				else:
					aworth = fiveassignment[i].apercentage * grouppercentage
					if aworth > percentage :
						percentage = aworth
						priority = fiveassignment[i]
			allAssignmentsfive.append(fiveassignment)

	context = {
		'assignmentName' : allAssignmentsfive,
		'highestWorth' : priority
	}
	return render(request, 'courses/dashboard.html', context)