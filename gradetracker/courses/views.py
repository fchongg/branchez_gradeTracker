from django.http import HttpResponse

def Course(request):
    return HttpResponse("Hello, you're at the courses page.")

def addCourses(request):
    return HttpResponse("Hello, you're at the add courses page.")