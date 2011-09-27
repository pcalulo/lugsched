from django.db import models

# Create your models here.
class University(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	termsPerYear = models.IntegerField('terms per year')
	
	def __unicode__(self):
		return self.name

	class Meta:
		# If we didn't do this, the plural name shown in the admin site
		# would be "Universitys"
		verbose_name_plural = 'Universities'


class UserProfile(models.Model):
	email = models.CharField(max_length=128)
	nickname = models.CharField(max_length=64)
	university = models.ForeignKey(University)
	
	def __unicode__(self):
		return '%s (%s)' % (self.nickname, self.email)


class Friendship(models.Model):
	user1 = models.ForeignKey(UserProfile, related_name='user1')
	user2 = models.ForeignKey(UserProfile, related_name='user2')


class Course(models.Model):
	code = models.CharField(max_length=32)
	name = models.CharField(max_length=64)
	description = models.CharField(max_length=200)
	university = models.ForeignKey(University)

	def __unicode__(self):
		return self.code


class Schedule(models.Model):
	creationDate = models.DateTimeField('date created')
	name = models.CharField(max_length=100)
	owner = models.ForeignKey(UserProfile)
	university = models.ForeignKey(University)

	def __unicode__(self):
		return '%s' % self.name


class Section(models.Model):
	name = models.CharField(max_length=16)
	course = models.ForeignKey(Course)
	enrollees = models.ManyToManyField(Schedule, through='Enrollment')

	def __unicode__(self):
		return '%s %s' % (self.course.code, self.name)


class Meeting(models.Model):
	section = models.ForeignKey(Section)
	startTime = models.DateTimeField('start time')
	endTime = models.DateTimeField('end time')
	days = models.CharField(max_length=7)

	def __unicode__(self):
		return 'Meeting for %s' % self.section


class Enrollment(models.Model):
	schedule = models.ForeignKey(Schedule)
	section = models.ForeignKey(Section)
	
	def __unicode__(self):
		return unicode(self.section)
		

