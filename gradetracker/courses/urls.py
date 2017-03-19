from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Course, name='Course'),
    # ex: /Courses/add/
    url(r'addCourses^$', views.addCourses, name='addCourses'),
]