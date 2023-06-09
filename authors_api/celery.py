import os

from celery import Celery
from django.conf import settings

# TODO: change this in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

app = Celery("authors_api")

# used to load the configuration from the Django settings
# module and the namespace arguments is used to avoid clashes between the celery configuration and the
# Django configuration.
app.config_from_object("django.conf:settings", namespace="CELERY")


# Autodiscover task is used to automatically discover tasks in all the installed Django
# applications.
# This is a convenient function that is equivalent to calling the task decorator on each of the tasks
# modules in the installed app setting.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)