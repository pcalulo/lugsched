
# Note: run this like so:
# ./manage.py shell < sample_data.py

from datetime import time
from core.models import *

uni_count = len(University.objects.all())
if (uni_count > 0):
    print 'Found at least one existing University!'
    print 'This script should only be used to quickly set up an empty database'
    return

uni = University()
uni.name = 'De La Salle University'
uni.address = '2401 Taft Avenue, Malate, Manila'
uni.termsPerYear = 3
uni.save()

course = Course()
course.code = 'COMPRO1'
course.name = 'Introduction to Computer Programming'
course.description = '...'
course.university = uni
course.save()

section = Section()
section.name = 'S22'
section.course = course
section.save()

meeting = Meeting()
meeting.section = section
meeting.startTime = time(8, 0)
meeting.endTime = time(9, 30)
meeting.hasMondays = True
meeting.hasThursdays = True
meeting.save()

