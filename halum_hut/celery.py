import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'halum_hut.settings')
app = Celery('halum_hut')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()