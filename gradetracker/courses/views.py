from django.http import HttpResponse

from .models import Course
from .models import AssessmentGroup
from .models import Assessment, AgType
from django.template import loader
from django.shortcuts import render
from itertools import chain


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

def courses(request, question_id):
	current_user = request.user
	if current_user.is_authenticated():
		# grab all the courses associated with that id
		all_courses = Course.object.get(uid=current_user.id)

	else:
		return HttpResponse("You're looking at question %s." % question_id)
    

def addCourses(request):
    return HttpResponse("Hello, you're at the add courses page.")



