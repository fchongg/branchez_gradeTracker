from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import django.utils.timezone
from django import forms
import datetime
from django.utils import timezone


class Course(models.Model):
    uid =  models.ForeignKey(User)
    cname = models.CharField(max_length=200, verbose_name='Course Name')
    term = models.CharField(max_length=2, verbose_name='Term')

    def get_all_courses(user_id):
        Course.objects.filter(uid = user_id)

    def __str__(self):
        return self.cname

class AgType(models.Model):
    agname = models.CharField(max_length=100)

    def __str__(self):
        return self.agname

class AssessmentGroup(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name = 'Course')
    agpercentage = models.PositiveSmallIntegerField(verbose_name = 'Percentage of Class')
    agtid = models.ForeignKey(AgType, verbose_name = 'Type of Assessment')

    def __unicode__(self):
        return self.agtid.agname

    def get_all_assignments_5_days(self, course_id):
        AssessmentGroup.objects.filter(cid = course_id, date__lt=timezone.now() - datetime.timedelta(days=5))


    def __str__(self):
        return self.agtid.agname

    def get_all_assignments(self, course_id):
        AssessmentGroup.objects.get(cid = course_id)

class Assessment(models.Model):
	aname = models.CharField(max_length=200, verbose_name='Name')
	agid = models.ForeignKey(AssessmentGroup, verbose_name='Type of Assessment')
	apercentage = models.PositiveSmallIntegerField(verbose_name='Percentage of Assessment Group')
	duedate = models.DateTimeField(default= django.utils.timezone.now, verbose_name='Due Date')
