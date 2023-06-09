# guarantee that celery app is always imported when Django starts.
from .celery import app as celery_app

__all__ = ("celery_app",)


# this is the code that will be executed when the celery worker is started.
# It will load the Django Settings module and then discover all the tasks in the installed Django apps.