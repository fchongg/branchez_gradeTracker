from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Course
from .models import AssessmentGroup
from .models import Assessment, AgType
from django.template import loader
from django.shortcuts import render
from .forms import CourseForm
from django.views.decorators.csrf import csrf_exempt
from itertools import chain

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
	print ("made it to add courses")
	course_debug = Course(uid_id=1, cname='trial', term='w1')
	course_debug.save()
	if request.method == 'POST':
		print("made it to post")
		form = CourseForm(request.POST, request.FILES or none)
		if form.is_valid():
			cname = request.POST.get('add_cname', '')
			print("made it to cname")
			term = request.POST.get('add_term', '')
			print("made it to term")
			course_obj = Course(cname=cname, term=term)
			
			
			return HttpResponse('home_courses/')

	else: 
		form = CourseForm()
	return render(request, 'courses/addcourse.html')



