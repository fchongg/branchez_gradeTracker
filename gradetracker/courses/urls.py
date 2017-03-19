from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^$', views.courses, name='courses'),
    # ex: /Courses/add/
    url(r'^addcourses/$', views.addcourses, name='addcourses'),
]