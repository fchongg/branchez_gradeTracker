from django.http import HttpResponse

from .models import Course
from .models import AssessmentGroup
from .models import Assessment
from django.template import loader
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, you're at the courses section")


def courseDetail(request):

    return HttpResponse();

def courses(request):
<<<<<<< HEAD



    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)



	current_user = request.user
	# template = loader.get_template('course')
	all_courses = Course.objects.filter(uid=1)

	context = {
       	'all_courses': all_courses,

   	}
	# 	if(all_courses == null):
	# 		#TODO: empty context here
	# else: 
	# 	# do nothing

	return render(request, 'courses/course.html', context)
=======


	return HttpResponse("courses")
>>>>>>> 33bb2a8ba4dc320cf345d661ef65a33a5f8b61ba

def addcourses(request):

    return render(request, 'courses/addcourses.html')

