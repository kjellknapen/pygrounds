import os
import sys

path = '/home/deploybot/pygrounds.knapenkjell.com/'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pygrounds.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()