import os, sys
sys.path.append('c:/Users/Akhyansh/Desktop/') os.environ['DJANGO_SETTINGS_MODULE'] = 'thought.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()