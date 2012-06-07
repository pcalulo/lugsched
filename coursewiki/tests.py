"""
Tests for the Course Wiki
"""

from django.test import TestCase

from django.contrib.auth.models import User
from coursewiki.models import *
from core.models import *

from datetime import datetime, time

import sample_data

def create_temp_university():
    uni = University()
    uni.name = 'Some University For Testing'
    uni.address = '1234 Example Avenue'

    # Create the user required to save the university
    user = User()
    user.username = 'Temp Guy'
    user.save()

    uni.update(user, 'Added temp university')

    return uni

def create_temp_course(uni):
    course = Course()

    course.university = uni
    course.code = 'EXAMPLE'
    course.name = 'An example course'
    course.description = 'Apple Banana Coconut'
    course.creation_date = datetime.now()
    course.update(uni.editor, 'Added temp course')

    return course

def create_temp_term(uni):
    term = Term()
    term.university = uni
    term.academic_year = 2012
    term.index = 1
    term.note = 'Lorem ipsum dolor sit amet...'

    term.update(uni.editor, 'Added temp term')

    return term

class CopyTest(TestCase):
    """
    Tests that check whether the data that gets copied into the archives is
    identical to the copy in core
    """

    def setUp(self):
        # Create the test user
        self.user = user = User()
        user.username = 'Tester'
        user.email = 'test@example.com'
        user.save()
        sample_data.add_wiki_data(user)

        self.temp_uni = create_temp_university()
        self.temp_term = create_temp_term(self.temp_uni)
        self.temp_course = create_temp_course(self.temp_uni)


    def test_university(self):
        universities = University.objects.all()

        uni = universities[0]
        orig_name = uni.name
        orig_address = uni.address

        appended_string = 'Testing'

        uni.name += appended_string
        uni.address += appended_string
        uni.update(self.user, appended_string)

        history = uni.get_history()

        latest = history[0]
        self.assertEqual(latest.name, orig_name + appended_string)
        self.assertEqual(latest.address, orig_address + appended_string)

        second_latest = history[1]
        self.assertEqual(second_latest.name, orig_name)
        self.assertEqual(second_latest.address, orig_address)

    def test_term(self):
        terms = Term.objects.all()

        term = terms[0]
        orig_uni = term.university
        orig_ay = term.academic_year
        orig_index = term.index
        orig_note = term.note

        temp_uni = self.temp_uni
        appended_string = 'Testing'

        term.university = temp_uni
        term.academic_year += 1
        term.index += 1
        term.note += appended_string
        term.update(self.user, 'Testing testing 1234')

        history = term.get_history()

        latest = history[0]
        self.assertEqual(latest.university, temp_uni)
        self.assertEqual(latest.academic_year, orig_ay + 1)
        self.assertEqual(latest.index, orig_index + 1)
        self.assertEqual(latest.note, orig_note + appended_string)

        second_latest = history[1]
        self.assertEqual(second_latest.university, orig_uni)
        self.assertEqual(second_latest.academic_year, orig_ay)
        self.assertEqual(second_latest.index, orig_index)
        self.assertEqual(second_latest.note, orig_note)

    def test_course(self):
        courses = Course.objects.all()

        course = courses[0]
        orig_uni = course.university
        orig_name = course.name
        orig_code = course.code
        orig_description = course.description
        orig_creation_date = course.creation_date

        temp_uni = self.temp_uni
        appended_string = 'Testing'
        current_date = datetime.now()

        course.university = temp_uni
        course.name += appended_string
        course.code += appended_string
        course.description += appended_string
        course.creation_date = datetime.now()
        course.update(self.user, 'Testing testing 1234')

        history = course.get_history()

        latest = history[0]
        self.assertEqual(latest.university, temp_uni)
        self.assertEqual(latest.name, orig_name + appended_string)
        self.assertEqual(latest.code, orig_code + appended_string)
        self.assertEqual(latest.description, orig_description + appended_string)
        # datetime.now() returns a datetime with microsecond precision. The
        # datetime in the course from the database only has second precision, so
        # the assertEqual for these is ommitted for simplicity. The asserts for
        # second_latest should cover the relevant code sufficiently, though.

        second_latest = history[1]
        self.assertEqual(second_latest.university, orig_uni)
        self.assertEqual(second_latest.name, orig_name)
        self.assertEqual(second_latest.code, orig_code)
        self.assertEqual(second_latest.description, orig_description)
        self.assertEqual(second_latest.creation_date, orig_creation_date)

    def test_section(self):
        sections = Section.objects.all()

        section = sections[0]
        orig_name = section.name
        orig_course = section.course
        orig_term = section.term

        temp_course = self.temp_course
        temp_term = self.temp_term
        appended_string = 'A'

        section.name += appended_string
        section.course = temp_course
        section.term = temp_term
        section.update(self.user, 'Testing testing 1234')

        history = section.get_history()

        latest = history[0]
        self.assertEqual(latest.name, orig_name + appended_string)
        self.assertEqual(latest.course, temp_course)
        self.assertEqual(latest.term, temp_term)

        second_latest = history[1]
        self.assertEqual(second_latest.name, orig_name)
        self.assertEqual(second_latest.course, orig_course)
        self.assertEqual(second_latest.term, orig_term)

    def test_meeting(self):
        meeting = Meeting()

        # The section we use here doesn't really matter; what matters is that we
        # have a section to work with
        meeting.section = Section.objects.all()[0]
        meeting.start_time = time(8, 0)
        meeting.end_time = time(9, 30)
        meeting.has_mondays = True
        meeting.has_wednesdays = True

        meeting.update(self.user, 'Add for testing')

        orig_start_time = meeting.start_time
        orig_end_time = meeting.end_time
        
        meeting.start_time = time(9, 40)
        meeting.end_time = time(11, 10)
        meeting.has_mondays = False
        meeting.has_tuesdays = True
        meeting.has_wednesdays = False
        meeting.has_thursdays = True
        meeting.has_fridays = True
        meeting.has_saturdays = True
        meeting.has_sundays = True

        meeting.update(self.user, 'Testing testing 1234')

        history = meeting.get_history()

        latest = history[0]
        self.assertEqual(meeting.start_time, latest.start_time)
        self.assertEqual(meeting.end_time, latest.end_time)
        self.assertEqual(meeting.has_mondays, latest.has_mondays)
        self.assertEqual(meeting.has_tuesdays, latest.has_tuesdays)
        self.assertEqual(meeting.has_wednesdays, latest.has_wednesdays)
        self.assertEqual(meeting.has_thursdays, latest.has_thursdays)
        self.assertEqual(meeting.has_fridays, latest.has_fridays)
        self.assertEqual(meeting.has_saturdays, latest.has_saturdays)
        self.assertEqual(meeting.has_sundays, latest.has_sundays)

        second_latest = history[1]
        self.assertEqual(second_latest.start_time, orig_start_time)
        self.assertEqual(second_latest.end_time, orig_end_time)
        self.assertTrue(second_latest.has_mondays)
        self.assertFalse(second_latest.has_tuesdays)
        self.assertTrue(second_latest.has_wednesdays)
        self.assertFalse(second_latest.has_thursdays)
        self.assertFalse(second_latest.has_fridays)
        self.assertFalse(second_latest.has_saturdays)
        self.assertFalse(second_latest.has_sundays)

