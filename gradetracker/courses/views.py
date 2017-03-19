from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Course
from .models import AssessmentGroup
from .models import Assessment
from django.template import loader
from django.shortcuts import render
from .forms import CourseForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

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
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			cname = request.POST.get('add_cname', '')
			term = request.POST.get('add_term', '')
			#assessments = request.POST.get('add_assessments','')
			course_obj = Course(cname=cname, term=term)
			course_obj.save()
			return HttpResponse('home_courses/')

	else: 
		form = CourseForm()
	return render(request, 'courses/addcourse.html')


