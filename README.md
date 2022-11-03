# Blogify
click on below blogify-logo to visit our website:

<a href="https://blogify-application.web.app/">
<img style="height:80px;width:auto;" alt="visit website" src="https://blogify-application.web.app/img/blogify_logo.acfb6c5c.png"/> 
</a>


### Description
Blogify is a blogging website built using Python Django framework (for backend development), vue.js framework for frontend developemnt.

### Usage
setting up the Django project:
* clone project from this repo using "git clone <repo>" command.
* create and start a virtual environment.
* after starting virtual environment and changing dir to our projects BASE dir, run command "pip install -r requirements.txt" (to install all dependencies).
* run these commmands to make migrations (ensure that sqlite is installed on your system)
python manage.py makemigrations
python manage.py migrate
* run command "python manage.py runserver" to start django server.

setting up the vue project:
* clone project from Blogify-frontend repo.
* ensure that npm is installed on your system.
* change urls for django app, in app the vue-components.
* run command "npm runserve" to start vue app.
