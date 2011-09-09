from core.models import *
from django.contrib import admin

class UniversityAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic Information', {'fields': ['name', 'address']}),
		('Further Details', {'fields': ['termsPerYear']})
	]

	list_display = ['name', 'address']

admin.site.register(University, UniversityAdmin)

admin.site.register(UserProfile)

# Add Friendship stuff here?

class CourseAdmin(admin.ModelAdmin):
	list_display = ['code', 'description']

admin.site.register(Course, CourseAdmin)

class EnrollmentInline(admin.StackedInline):
	model = Enrollment
	extra=3
class ScheduleAdmin(admin.ModelAdmin):
	inlines = [EnrollmentInline]

admin.site.register(Schedule, ScheduleAdmin)

admin.site.register(Section)

class MeetingAdmin(admin.ModelAdmin):
	list_display = ['section', 'startTime', 'endTime']

admin.site.register(Meeting, MeetingAdmin)

# Add Enrollment stuff here?

