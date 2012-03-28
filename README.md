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
 * being rewritten from the ground up, to be independent of Google App Engine

We are performing this rewrite as we are not comfortable with the potential
lock-in that we would experience should we continue with the original,
GAE-hosted web app, which was named forever-alone. The rewrite is expected to go
faster and more smoothly than the initial development, as a lot of the design
has been ironed out.


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

