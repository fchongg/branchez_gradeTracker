from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import django.utils.timezone



TERM_CHOICES = (
    ('W1', 'W2', 'S1', 'S2'),
    )
class Course(models.Model):
    uid =  models.ForeignKey(User)
    cname = models.CharField(max_length=200)
    term = models.CharField(max_length=2)

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['cname', 'term']

class AgType(models.Model):
    agname = models.CharField(max_length=100)


class AssessmentGroup(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    agpercentage = models.PositiveSmallIntegerField()
    agtid = models.ForeignKey(AgType)


    def __unicode__(self):
        # model = AgType
        name = Course.objects.get(id=self.agtid)
        # name = self.getName()
        # name = AgType.objects.get(id=self.agtid)
        # print(name)
        # name = str(typeobj['agname'])
        # print nameG
        return str(self.agpercentage)

    def get_all_assignments(self, course_id):
        AssessmentGroup.objects.get(cid = course_id);

class Assessment(models.Model):
	aname = models.CharField(max_length=200, verbose_name='Name')
	agid = models.ForeignKey(AssessmentGroup, verbose_name='Type of Assessment')
	apercentage = models.PositiveSmallIntegerField(verbose_name='Percentage of Assessment Group')
	duedate = models.DateTimeField(default= django.utils.timezone.now, verbose_name='Due Date')
