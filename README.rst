====================================
Deployment package for Hello Web App
====================================

This package will install all the necessary packages for deploying a Django
project on Heroku. Developed for the `Hello Web App <http://hellowebapp.com>`_
book, which teaches beginner web app development using Python and Django.

Packages installed:

- `gunicorn <http://gunicorn.org/>`_
- `dj-database-url <https://github.com/kennethreitz/dj-database-url>`_
- `whitenoise <https://warehouse.python.org/project/whitenoise/>`_

This package is similar to `django-toolbelt
<https://pypi.python.org/pypi/django-toolbelt/0.0.1/>`_ but does not require
psycopg2 as a dependency and uses whitenoise rather than dj-static.

License
-------

This project is licensed under the MIT open source license.
