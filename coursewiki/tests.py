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


    def test_university(self):
        universities = University.objects.all()

        uni = universities[0]
        orig_name = uni.name
        orig_address = uni.address

        appended_string = 'Testing'

        uni.name += appended_string
        uni.address += appended_string
        uni.update(self.user, appended_string)

        # The update() calls are extremely close to each other, so we can't
        # order by edit_timestamp
        history = uni.archiveduniversity_set.all().order_by('-pk')

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

        temp_uni = create_temp_university()
        appended_string = 'Testing'

        term.university = temp_uni
        term.academic_year += 1
        term.index += 1
        term.note += appended_string
        term.update(self.user, 'Testing testing 1234')

        # The update() calls are extremely close to each other, so we can't
        # order by edit_timestamp.
        history = term.archivedterm_set.all().order_by('-pk')

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

        temp_uni = create_temp_university()
        appended_string = 'Testing'
        current_date = datetime.now()

        course.university = temp_uni
        course.name += appended_string
        course.code += appended_string
        course.description += appended_string
        course.creation_date = datetime.now()
        course.update(self.user, 'Testing testing 1234')

        history = course.archivedcourse_set.all().order_by('-pk')

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

