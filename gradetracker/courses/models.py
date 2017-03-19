from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    cid = models.IntegerField()
    uid =  models.ForeignKey(User)
    cname = models.CharField(max_length=8)
    term = models.CharField(max_length=2)

class AgType(models.Model):
    agtid = models.IntegerField()
    agname = models.CharField(max_length=100)

class AssessmentGroup(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    agid = models.IntegerField()
    agpercentage = models.PositiveSmallIntegerField()
    agtid = models.ForeignKey(AgType)

class Assessment(models.Model):
	agtid = models.ForeignKey(AgType)
	aname = models.CharField(max_length=200)
	agid = models.ForeignKey(AssessmentGroup)
	apercentage = models.PositiveSmallIntegerField()
	duedate = models.DateTimeField('Due Date')

