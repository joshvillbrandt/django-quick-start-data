django-quick-start-data
=======================

This is a Django project template to create a data-only app with an api.

This package is intended to jump-start the development of a data-only application. No user interface is intended to be supplied with this server. The division of application and and user interface components allows these parts of an application to evolve independently. It also requires the developer to build a healthy API which then allows the data stored here to easily be used by other applications.

# Setup

This app requires Django >= 1.5 and Tastypie. If you don't have these things installed, run the following (sudo might be required):

    sudo apt-get install python-pip
    sudo pip install django==1.5 python-dateutil python-mimeparse django-tastypie

Then start your project and add your custom data models.

    django-admin.py startproject --template=https://github.com/joshvillbrandt/django-quick-start-data/archive/master.zip --extension=py,html site_name

When you are ready to roll, sync your database and start the server.

    cd priorityDB
    python manage.py syncdb
    python manage.py runserver 0.0.0.0:8000
