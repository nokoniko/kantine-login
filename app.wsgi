import sys
import site
import os

site.addsitedir('/var/www/test/venv/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/test')
os.chdir('/var/www/test')

os.environ['VIRTUAL_ENV'] = '/var/www/test/venv'
os.environ['PATH'] = '/var/www/test/venv/bin:' + os.environ['PATH']

from app import app as application
