from core.models import *
from django.contrib import admin

class UniversityAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic Information', {'fields': ['name', 'address']}),
		('Further Details', {'fields': ['termsPerYear']})
	]

admin.site.register(University, UniversityAdmin)
admin.site.register(UserProfile)
# Friendship
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(Section)
admin.site.register(Meeting)
# Enrollment

