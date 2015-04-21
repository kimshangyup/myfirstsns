


import os
import sys
sys.path.append('/home/venture/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


