from coursewiki.models import *
from django.contrib import admin

class ArchivedUniversityAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic Information', {'fields': ['name', 'address']}),
		('Further Details', {'fields': ['terms_per_year']})
	]

	list_display = ['name', 'address']

admin.site.register(ArchivedUniversity, ArchivedUniversityAdmin)

class ArchivedCourseAdmin(admin.ModelAdmin):
	list_display = ['code', 'description']

admin.site.register(ArchivedCourse, ArchivedCourseAdmin)

admin.site.register(ArchivedSection)

class ArchivedMeetingAdmin(admin.ModelAdmin):
	list_display = ['section', 'start_time', 'end_time']

admin.site.register(ArchivedMeeting, ArchivedMeetingAdmin)

