forever-alone
=============

What is forever-alone?
-----------------------------
Forever-Alone is a web app for finding common courses and free time among you
and your friends.

It aims to be a more useful replacement for the deluge of screenshots of
spreadsheets with schedule info that gets posted to Facebook/Google+ every
time a new term begins.


forever-alone is currently...
-----------------------------

 * being rewritten from the ground up, to be independent of Google App Engine

We are performing this rewrite as we are not comfortable with the potential lock-in
that we would experience should we continue with the original, GAE-hosted web app.
The rewrite is expected to go faster and more smoothly than the initial development,
as a lot of the design has been ironed out.


The Django Apps
---------------
**core** - Low-level, inner workings stuff belongs in here. Mainly the models.

**auth** - Handles user login, logout, and registration.

**appbase** - Implements the home page.

**api** - Provides the RESTful API, through which other apps can access forever-alone.

**schedules** - Provides the primary user-facing functionality of falone



Credit where credit is due
--------------------------

"Forever Alone" (no, not this app) is an Internet meme. See 
[this Know Your Meme page][kymfa]. The name was chosen due to its contrast
between the very social-oriented goal of this app, and the antisocial, lonely
nature of the Forever Alone meme.

[kymfa]: http://knowyourmeme.com/memes/forever-alone
