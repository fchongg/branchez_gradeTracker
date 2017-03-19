from django.http import HttpResponse

from .models import Course
from .models import AssessmentGroup
from .models import Assessment
from django.template import loader


def index(request):
    return HttpResponse("Hello, you're at the courses section")


def courseDetail(request):

    return HttpResponse();

def courses(request, question_id):
	current_user = request.user
	template = loader.get_template('course')

	if current_user.is_authenticated():
		# grab all the courses associated with that id
		all_courses = Course.object.get(uid=current_user.id)
		if(all_courses == null):
			#TODO: empty context here
	else: 
		# do nothing

	return HttpResponse(template.render(_,request))

def addCourses(request):
    return HttpResponse("Hello, you're at the add courses page.")


