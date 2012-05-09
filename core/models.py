from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

################################################################################
# Log-keeping
# All base models inherit from this, allowing all versioned data to have an edit
# message.
################################################################################
class WikiModel(models.Model):
    editor = models.ForeignKey(User)
    edit_message = models.CharField(max_length=255)
    edit_timestamp = models.DateTimeField()

    def set_edit_message(self, editor, message):
        self.editor = editor
        self.edit_message = message
        self.edit_timestamp = datetime.now()


################################################################################
# Base models. Core and coursewiki models inherit from these.
################################################################################

class BaseUniversity(WikiModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

    class Meta:
        # If we didn't do this, the plural name shown in the admin site
        # would be "Universitys"
        verbose_name_plural = 'Universities'


class BaseTerm(WikiModel):
    university = models.ForeignKey('University')

    # This is the starting year of the academic year that this term belongs to.
    # For example, if this term belongs to AY 2011-2012, this value should be
    # set to 2011.
    academic_year = models.IntegerField()

    index = models.IntegerField()
    note = models.CharField(max_length=1000)

    def __unicode__(self):
        return '%s AY %d - %d Term %d' % (
                    self.university,
                    self.academic_year,
                    self.academic_year + 1,
                    self.index,
                )


class BaseCourse(WikiModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    university = models.ForeignKey('University')

    creation_date = models.DateTimeField('date created')

    def __unicode__(self):
        return self.code


class BaseSection(WikiModel):
    name = models.CharField(max_length=16)
    course = models.ForeignKey('Course')
    term = models.ForeignKey('Term')

    def __unicode__(self):
        return '%s %s' % (self.course.code, self.name)


class BaseMeeting(WikiModel):
    section = models.ForeignKey('Section')
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


################################################################################
# Core models
# These hold the latest copies of course data.
################################################################################

class University(BaseUniversity):
    def update(self, user, message):
        """
        Copies the University into the archives, then saves it.
        """
        self.set_edit_message(user, message)
        self.save()

        archived_uni = ArchivedUniversity()
        archived_uni.copy(self)
        archived_uni.save()


class Term(BaseTerm):
    def update(self, user, message):
        """
        Copies the Term into the archives, then saves it.
        """
        self.set_edit_message(user, message)
        self.save()

        archived_term = ArchivedTerm()
        archived_term.copy(self)
        archived_term.save()


class Course(BaseCourse):
    def update(self, user, message):
        """
        Copies the Course into the archives, then saves it.
        """
        self.set_edit_message(user, message)
        self.save()

        archived_course = ArchivedCourse()
        archived_course.copy(self)
        archived_course.save()


class Section(BaseSection):
    def update(self, user, message):
        """
        Copies the Section into the archives, then saves it.
        """
        self.set_edit_message(user, message)
        self.save()

        archived_section = ArchivedSection()
        archived_section.copy(self)
        archived_section.save()


class Meeting(BaseMeeting):
    def update(self, user, message):
        """
        Copies the Meeting into the archives, then saves it.
        """
        self.set_edit_message(user, message)
        self.save()

        archived_meeting = ArchivedMeeting()
        archived_meeting.copy(self)
        archived_meeting.save()


################################################################################
# User-specific models
# These are only modifiable by a single user, and does not need to be versioned.
################################################################################


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


class Schedule(models.Model):
    creationDate = models.DateTimeField('date created')
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserProfile)
    university = models.ForeignKey(University)
    classes = models.ManyToManyField(Section)

    def __unicode__(self):
        return '%s' % self.name


############################################################################
# IMPORTANT!
# There is a circular dependency between core models and coursewiki models.
# This is intentional.
# To prevent problems, this import must be done after all core models have
# been declared.
#
# This is required because the coursewiki models inherit from the base models
# which are declared in this file. Importing them here means that the classes
# have already been declared, allowing the coursewiki models code to load
# without errors.

from coursewiki.models import *

############################################################################

