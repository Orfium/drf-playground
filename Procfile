release: python manage.py migrate
web: ddtrace-run gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker
worker: ddtrace-run celery worker --app=config.celery_app --loglevel=info
beat: ddtrace-run celery beat --app=config.celery_app --loglevel=info
