import os
import sys

path = '/home/deploybot/pygrounds.knapenkjell.com/pygrounds'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pygrounds.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()