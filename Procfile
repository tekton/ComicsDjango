web: gunicorn_django --workers=3 --daemon --pid=g.pid -b 0.0.0.0:8000 --log-syslog --access-logfile access.log --error-logfile error.log
celeryd: python manage.py celeryd -E -B --loglevel=INFO --autoreload
