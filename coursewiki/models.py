from django.db import models
from django.contrib.auth.models import User
from core.models import *

# The Course Wiki's models are primarily about storing old revisions of
# LugSched's data. This lets us keep track of who did which revision, as
# well as allowing us to revert to older revisions in case of vandalism.
#
# When updating models in core, remember to also do the relevant updates
# to models in this file.

class EditLog(models.Model):
    user = models.ForeignKey(User)
    edit_timestamp = models.DateTimeField()

class ArchivedUniversity(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

    def copy(self, university):
        self.name = university.name
        self.address = university.address
    
    class Meta:
        # If we didn't do this, the plural name shown in the admin site
        # would be "Universitys"
        verbose_name_plural = 'Archived universities'


class ArchivedTerm(models.Model):
    university = models.ForeignKey(University)
    academic_year = models.IntegerField()
    index = models.IntegerField()
    note = models.CharField(max_length=1000)


class ArchivedCourse(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    university = models.ForeignKey(University)

    creation_date = models.DateTimeField('date created')
    creator = models.ForeignKey(User)

    def copy(self, course):
        self.code = course.code
        self.name = course.name
        self.description = course.description
        self.university = course.university
        self.creation_date = course.creation_date

    def __unicode__(self):
        return self.code


class ArchivedSection(models.Model):
    name = models.CharField(max_length=16)
    course = models.ForeignKey(Course)

    def copy(self, section):
        self.name = section.name
        self.course = section.course

    def __unicode__(self):
        return '%s %s' % (self.course.code, self.name)


class ArchivedMeeting(models.Model):
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

    def copy(self, meeting):
        self.section = meeting.section
        self.start_time = meeting.start_time
        self.end_time = meeting.end_time

    def __unicode__(self):
        return 'Meeting for %s' % self.section

    def to_dict(self):
        mDict = {}
        mDict['startTime'] = self.startTime
        mDict['endTime'] = self.endTime
        mDict['days'] = self.days
        return mDict

