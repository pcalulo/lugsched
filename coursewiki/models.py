from django.db import models
from django.contrib.auth.models import User
from core.models import *

# The Course Wiki's models are primarily about storing old revisions of
# LugSched's data. This lets us keep track of who did which revision, as
# well as allowing us to revert to older revisions in case of vandalism.

class EditLog(models.Model):
    user = models.ForeignKey(User)
    edit_timestamp = models.DateTimeField()


class ArchivedUniversity(BaseUniversity):
    def copy(self, university):
        self.name = university.name
        self.address = university.address
    
    class Meta:
        # If we didn't do this, the plural name shown in the admin site
        # would be "Universitys"
        verbose_name_plural = 'Archived universities'


class ArchivedTerm(BaseTerm):
    def copy(self, term):
        return


class ArchivedCourse(models.Model):
    def copy(self, course):
        self.code = course.code
        self.name = course.name
        self.description = course.description
        self.university = course.university
        self.creation_date = course.creation_date


class ArchivedSection(models.Model):
    def copy(self, section):
        self.name = section.name
        self.course = section.course
        self.term = section.term


class ArchivedMeeting(models.Model):
    def copy(self, meeting):
        self.section = meeting.section
        self.start_time = meeting.start_time
        self.end_time = meeting.end_time

