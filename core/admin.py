from core.models import *
from django.contrib import admin

class UniversityAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic Information', {'fields': ['name', 'address']}),
		('Further Details', {'fields': ['terms_per_year']})
	]

	list_display = ['name', 'address']

admin.site.register(University, UniversityAdmin)

admin.site.register(UserProfile)

# Add Friendship stuff here?

class CourseAdmin(admin.ModelAdmin):
	list_display = ['code', 'description']

admin.site.register(Course, CourseAdmin)

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ['name', 'owner', 'university']

admin.site.register(Schedule, ScheduleAdmin)

admin.site.register(Section)

class MeetingAdmin(admin.ModelAdmin):
	list_display = ['section', 'start_time', 'end_time']

admin.site.register(Meeting, MeetingAdmin)

# Add Enrollment stuff here?

