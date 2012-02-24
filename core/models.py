from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    terms_per_year = models.IntegerField('terms per year')
    
    def __unicode__(self):
        return self.name

    class Meta:
        # If we didn't do this, the plural name shown in the admin site
        # would be "Universitys"
        verbose_name_plural = 'Universities'


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    nickname = models.CharField(max_length=64)
    university = models.ForeignKey(University)

    # This is, apparently, the recommended way to create a many-to-many
    # relationship with the same class - see ManyToManyField docs.
    # Also, blank and null must be true, so the admin site and the database,
    # respectively, will allow us to leave fields empty. For more details, see:
    # http://www.b-list.org/weblog/2006/jun/28/django-tips-difference-between-blank-and-null/
    friends = models.ManyToManyField('self', blank=True, null=True)
    current_schedule = models.ForeignKey('Schedule', blank=True, null=True)
    
    def __unicode__(self):
        return '%s (%s)' % (self.nickname, self.user)


class Course(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.code


class Section(models.Model):
    name = models.CharField(max_length=16)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return '%s %s' % (self.course.code, self.name)

    def to_dict(self):
        sDict = {}
        meetings = self.meeting_set.all()
        cleanedMeetings = []

        # We need to remove some Django stuff that gets serialized along with the
        # rest of the data
        for meeting in meetings:
            cleanedMeetings.append(meeting.to_dict())

        sDict['meetings'] = cleanedMeetings
        sDict['section'] = self.name
        sDict['courseCode'] = self.course.code
        sDict['courseName'] = self.course.name
        return sDict


class Schedule(models.Model):
    creationDate = models.DateTimeField('date created')
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserProfile)
    university = models.ForeignKey(University)
    classes = models.ManyToManyField(Section)

    def __unicode__(self):
        return '%s' % self.name


class Meeting(models.Model):
    section = models.ForeignKey(Section)
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')

    has_mondays = models.BooleanField(default=False)
    has_tuesdays = models.BooleanField(default=False)
    has_wednesdays = models.BooleanField(default=False)
    has_thursdays = models.BooleanField(default=False)
    has_fridays = models.BooleanField(default=False)
    has_saturdays = models.BooleanField(default=False)
    has_sundays = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Meeting for %s' % self.section

    def to_dict(self):
        mDict = {}
        mDict['startTime'] = self.startTime
        mDict['endTime'] = self.endTime
        mDict['days'] = self.days
        return mDict

