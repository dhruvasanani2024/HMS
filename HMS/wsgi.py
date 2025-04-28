"""
WSGI config for HMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HMS.settings')

# Vercel expects the application callable to be named 'application'
application = get_wsgi_application()


# Vercel expects either 'app' or 'handler'
handler = application  # This is important for Vercel