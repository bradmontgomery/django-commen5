=============
{% commen5 %}
=============

Do you keep typing ``{% commen5 %}`` instead of ``{% comment %}``?  If so, then this app is for you!


Features
--------

* Lets you use ``{% commen5 %}`` instead of ``{% comment %}``


Installation
------------

To install from the current repository::

    pip install git+https://github.com/bradmontgomery/django-commen5/


Usage
-----

Include ``comment5`` in ``INSTALLED_APPS``, then in any template, load the ``commen5_tags`` library::

    {% load commen5_tags %}

Now, comment away with::

    {% commen5 %}
        blah blah blah blah
    {% endcommen5 %}


Disclaimer
----------
This is a joke. Don't really use this.
