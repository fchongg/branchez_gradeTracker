from django.http import HttpResponse


from .models import Course
from .models import AssessmentGroup
from .models import Assessment


def index(request):
    return HttpResponse("Hello, you're at the courses section")


def courseDetail(request):
    return HttpResponse();

def courses(request, question_id):
	current_user = request.user
	if current_user.is_authenticated():
		# grab all the courses associated with that id
		all_courses = Course.object.get(uid=current_user.id)
	else:
		return HttpResponse("You're looking at question %s." % question_id)
    
def addCourses(request):
    return HttpResponse("Hello, you're at the add courses page.")


