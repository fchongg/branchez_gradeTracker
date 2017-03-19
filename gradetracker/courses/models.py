from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone



class Course(models.Model):
    uid =  models.ForeignKey(User)
    cname = models.CharField(max_length=8)
    term = models.CharField(max_length=2)


class AgType(models.Model):
    agname = models.CharField(max_length=100)


class AssessmentGroup(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    agpercentage = models.PositiveSmallIntegerField()
    agtid = models.ForeignKey(AgType)

    def get_all_assignments(self, course_id):
        AssessmentGroup.objects.get(cid = course_id);

class Assessment(models.Model):
	agtid = models.ForeignKey(AgType)
	aname = models.CharField(max_length=200)
	agid = models.ForeignKey(AssessmentGroup)
	apercentage = models.PositiveSmallIntegerField()
	duedate = models.DateTimeField('Due Date', default= django.utils.timezone.now)
