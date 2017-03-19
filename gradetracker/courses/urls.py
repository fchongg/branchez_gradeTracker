from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<course_id>[0-9]+)/$', views.courseDetail, name= 'courseDetail'),
    # url(r'^$', views.index, name='index'),
    url(r'^home_courses/$', views.courses, name='courses'),
    url(r'^$', views.Course, name='Course'),
    # ex: /Courses/add/
    # url(r'^addcourses/$', views.addcourses, name='addcourses'),
    url(r'^addassessment/$', views.addAssessment, name='addassessment')
]