.. image:: https://travis-ci.org/gunthercox/django_chatterbot.svg?branch=master
    :target: https://travis-ci.org/gunthercox/django_chatterbot

=================
Django ChatterBot
=================

This is a Django project that makes it possible to create a simple chat bot web
app using Django_, `Django REST framework`_ and ChatterBot_.

Installation
------------

   pip install django-chatterbot

Quick start
-----------

1. Add "django_chatterbot" to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = (
       ...
       'django_chatterbot',
   )

2. Include the django_chatterbot URLconf in your project urls.py like this::

   url(r'^chatterbot/', include('django_chatterbot.urls')),

3. Run `python manage.py migrate` to create the chatterbot models.

4. POST to http://127.0.0.1:8000/chatterbot/ to start a conversation.

   {'text': 'Hello, how are you?'}

.. _Django: https://www.djangoproject.com
.. _Django REST framework: http://www.django-rest-framework.org
.. _ChatterBot: https://github.com/gunthercox/ChatterBot
