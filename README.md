The project currently known as LugSched
=============
(and formerly known as forever-alone)

What is LugSched?
-----------------------------
LugSched is a web app for finding common courses and free time among you
and your friends. It aims to be a more useful replacement for the deluge of
screenshots of spreadsheets with schedule info that gets posted to
Facebook/Google+ every time a new term begins.

The name is not final, but it sure as hell makes the project much easier to
talk about while walking from class to class...


LugSched is currently...
-----------------------------
 * being actively developed as a hobby project


Required Python Packages
-----------------------------
1. **Django**, of course
2. **django-piston**, for easy RESTful APIs
3. **markdown**, for convenient text formatting

You can easily install this using easy\_install, like so:

    sudo easy_install Django django-piston markdown

easy\_install should be readily available from your distro's package
repositories.


The Django Apps
---------------
**core** - Low-level, inner workings stuff belongs in here. Mainly the models.

**auth** - Handles user login, logout, and registration.

**appbase** - Implements the home page.

**api** - Provides the RESTful API, through which other apps can access
LugSched.

**schedules** - Provides the primary user-facing functionality of LugSched, i.e.
schedule CRUD operations

**coursewiki** - The course data crowdsourcing tool on which our course-finding
functionality will depend

