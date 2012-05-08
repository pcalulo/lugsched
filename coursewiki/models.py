from django.db import models
from django.contrib.auth.models import User
from core.models import *

# The Course Wiki's models are primarily about storing old revisions of
# LugSched's data. This lets us keep track of who did which revision, as
# well as allowing us to revert to older revisions in case of vandalism.


class ArchivedUniversity(BaseUniversity):
    parent = models.ForeignKey(University)

    def copy(self, university):
        self.parent = university

        self.name = university.name
        self.address = university.address
        self.set_edit_message(university.editor, university.message)
    
    class Meta:
        # If we didn't do this, the plural name shown in the admin site
        # would be "Universitys"
        verbose_name_plural = 'Archived universities'


class ArchivedTerm(BaseTerm):
    parent = models.ForeignKey(Term)

    def copy(self, term):
        self.parent = term

        self.university = term.university
        self.academic_year = term.academic_year
        self.index = term.index
        self.note = term.note
        self.set_edit_message(term.get_edit_message_tuple())


class ArchivedCourse(BaseCourse):
    parent = models.ForeignKey(Course)

    def copy(self, course):
        self.parent = course

        self.code = course.code
        self.name = course.name
        self.description = course.description
        self.university = course.university
        self.creation_date = course.creation_date
        self.set_edit_message(course.get_edit_message_tuple())


class ArchivedSection(BaseSection):
    parent = models.ForeignKey(Section)

    def copy(self, section):
        self.parent = section

        self.name = section.name
        self.course = section.course
        self.term = section.term
        self.set_edit_message(section.get_edit_message_tuple())


class ArchivedMeeting(BaseMeeting):
    parent = models.ForeignKey(Meeting)

    def copy(self, meeting):
        self.parent = meeting

        self.section = meeting.section
        self.start_time = meeting.start_time
        self.end_time = meeting.end_time

        self.has_mondays = meeting.has_mondays
        self.has_tuesdays = meeting.has_tuesdays
        self.has_wednesdays = meeting.has_wednesdays
        self.has_thursdays = meeting.has_thursdays
        self.has_fridays = meeting.has_fridays
        self.has_saturdays = meeting.has_saturdays
        self.has_sundays = meeting.has_sundays

        self.set_edit_message(meeting.get_edit_message_tuple())

