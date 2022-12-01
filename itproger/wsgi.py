"""
WSGI config for itproger project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itproger.settings')

application = get_wsgi_application()

import os, sys
virtual_env = os.path.expanduser('~/PycharmProjects/django-site/venv')
activate_this = os.path.join(virtual_env, 'bin/activate_this.py')
print(activate_this)
exec(open(activate_this).read(), dict(__file__=activate_this))
sys.path.insert(0, os.path.expanduser('~/PycharmProjects/django-site/itproger'))