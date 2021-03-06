from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<course_id>[0-9]+)/$', views.courseDetail, name= 'courseDetail'),
    # url(r'^$', views.index, name='index'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^$', views.Course, name='Course'),

    # ex: /Courses/add/
    url(r'^addcourses/$', views.addcourses, name='addcourses'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^addassessment/$', views.addAssessment, name='addassessment'),
    url(r'^(?P<course_id>[0-9]+)/addgroup/$', views.addAssessmentGroup, name='addgroup')
]