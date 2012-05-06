from django.db import models
from django.contrib.auth.models import User

# This file contains LugSched's core data models.
#
# When updating models in this file, please also update the relevant models for
# the coursewiki archive (in coursewiki/models.py)
#
# The above only applies to models that are used by the wiki.


class University(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

    class Meta:
        # If we didn't do this, the plural name shown in the admin site
        # would be "Universitys"
        verbose_name_plural = 'Universities'


class Term(models.Model):
    university = models.ForeignKey(University)
    index = models.IntegerField()
    note = models.CharField(max_length=1000)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    nickname = models.CharField(max_length=64)
    university = models.ForeignKey(University)

    # This is, apparently, the recommended way to create a many-to-many
    # relationship with the same class - see ManyToManyField docs.
    # Also, blank and null must be true, so the admin site and the database,
    # respectively, will allow us to leave fields empty. For more details, see:
    # http://www.b-list.org/weblog/2006/jun/28/django-tips-difference-between-blank-and-null/
    friends = models.ManyToManyField('self', blank=True, null=True)
    current_schedule = models.ForeignKey('Schedule', blank=True, null=True)
    
    def __unicode__(self):
        return '%s (%s)' % (self.nickname, self.user)


class Course(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    university = models.ForeignKey(University)

    creation_date = models.DateTimeField('date created')
    creator = models.ForeignKey(User)

    def __unicode__(self):
        return self.code


class Section(models.Model):
    name = models.CharField(max_length=16)
    course = models.ForeignKey(Course)
    term = models.ForeignKey(Term)

    def __unicode__(self):
        return '%s %s' % (self.course.code, self.name)


class Schedule(models.Model):
    creationDate = models.DateTimeField('date created')
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserProfile)
    university = models.ForeignKey(University)
    classes = models.ManyToManyField(Section)

    def __unicode__(self):
        return '%s' % self.name


class Meeting(models.Model):
    section = models.ForeignKey(Section)
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')

    has_mondays = models.BooleanField(default=False)
    has_tuesdays = models.BooleanField(default=False)
    has_wednesdays = models.BooleanField(default=False)
    has_thursdays = models.BooleanField(default=False)
    has_fridays = models.BooleanField(default=False)
    has_saturdays = models.BooleanField(default=False)
    has_sundays = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Meeting for %s' % self.section

    def to_dict(self):
        mDict = {}
        mDict['startTime'] = self.startTime
        mDict['endTime'] = self.endTime
        mDict['days'] = self.days
        return mDict

