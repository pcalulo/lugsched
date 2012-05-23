"""
Tests for the Course Wiki
"""

from django.test import TestCase

from django.contrib.auth.models import User
from coursewiki.models import *
from core.models import *

import sample_data

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

        uni.name = uni.name + appended_string
        uni.address = uni.address + appended_string
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

