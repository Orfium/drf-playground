release: python manage.py migrate
web: ddtrace-run gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker
worker: ddtrace-run celery --app=config.celery_app worker --loglevel=info
beat: ddtrace-run celery --app=config.celery_app beat --loglevel=info
