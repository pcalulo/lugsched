
# Note: run this like so:
# ./manage.py shell < sample_data.py

from datetime import time
from core.models import *
from django.contrib.auth.models import User
from datetime import datetime

uni_count = len(University.objects.all())
if (uni_count > 0):
    print 'Found at least one existing University!'
    print 'This script should only be used to quickly set up an empty database'
    sys.exit(1)

user_count = len(User.objects.all())
if (user_count == 0):
    print 'No users found!'
    print 'Please configure a superuser - The user with ID 0 will be assumed to be the admin'
    sys.exit(1)

uni = University()
uni.name = 'De La Salle University'
uni.address = '2401 Taft Avenue, Malate, Manila'
uni.terms_per_year = 3
uni.save()

user = User.objects.all()[0]
profile = UserProfile()
profile.user = user
profile.nickname = 'Pat'
profile.university = uni
profile.save()

course = Course()
course.code = 'THEORDT'
course.name = 'Theory of Reddit'
course.description = 'An in-depth course on Turing machines and Reddit'
course.university = uni
course.creation_date = datetime.now()
course.save()

section = Section()
section.name = 'S22'
section.course = course
section.save()

meeting = Meeting()
meeting.section = section
meeting.start_time = time(8, 0)
meeting.end_time = time(9, 30)
meeting.has_mondays = True
meeting.has_thursdays = True
meeting.save()

