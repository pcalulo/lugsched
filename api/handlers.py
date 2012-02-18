from piston.handler import BaseHandler
from core.models import *

class UniversityHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = University

    def read(self, request, uni_id=None):
        base = University.objects
        if uni_id:
            return base.get(pk=uni_id)
        else:
            return base.all()

class UniversityCourseHandler(BaseHandler):
    allowed_methods = ('GET',)
    fields = ('id', 'code', 'name', 'description')
    model = Course

    def read(self, request, uni_id, course_id=None):
        if course_id:
            if not isinstance(course_id, int):
                return Course.objects.get(university__pk=uni_id, code=course_id)
            else:
                course = Course.objects.get(pk=course_id)
        else:
            return Course.objects.filter(university__pk=uni_id)
        return None

class UserProfileHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = UserProfile

    def read(self, request, profile_id=None):
        if profile_id:
            return UserProfile.objects.get(pk=profile_id)
        return None

class CourseHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Course
    exclude = ('university')

    def read(self, request, course_id=None, uni_id=None):
        if course_id:
            # If given a course ID, return that
            # e.g. /api/course/1/
            return Course.objects.get(pk=course_id)
        elif uni_id:
            # If given a university ID, return all known courses for that university
            # e.g. /api/university/1/courses/
            return Course.objects.filter(university__pk=uni_id)
        else:
            # If we're not given anythin at all, return all known courses for the
            # user's university
            user_profile = request.user.get_profile()
            uni = user_profile.university
            return Course.objects.filter(university=uni)

class ScheduleHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Schedule
    fields = ('university', 'creationDate', 'name', 'classes')
    
    def read(self, request, schedule_id=None):
        if schedule_id:
            schedule = Schedule.objects.get(pk=schedule_id)
    
            enrollments = Enrollment.objects.filter(schedule=schedule)
            classes = []
            for enrollment in enrollments:
                section = enrollment.section.to_dict()
                classes.append(section)
    
            schedule.classes = classes
            return schedule
        else:
            schedules = Schedule.objects.all()
            return schedules

