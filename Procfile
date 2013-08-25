web: sudo python manage.py runfcgi method=threaded host=127.0.0.1 port=8000 pidfile=g.pid outlog=output.log errlog=error.log
celeryd: python manage.py celeryd -E -B --loglevel=INFO --autoreload
