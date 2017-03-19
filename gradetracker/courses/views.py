from django.http import HttpResponse

from .models import Course
from .models import AssessmentGroup
from .models import Assessment

def courses(request):
	#current_user = request.user
	#if current_user.is_authenticated():
		# grab all the courses associated with that id
	#	all_courses = Course.object.get(uid=current_user.id)
	#else: 
		# do nothing
    return HttpResponse("Hello, you're looking at courses page")
    
def addcourses(request):
    return render(request, 'courses/addcourses.html')
