from celery import Celery
from app.core.config import settings


celery = Celery("worker", broker=settings.CELERY_BROKER)

celery.conf.task_routes = {settings.CELERY_TASK: settings.CELERY_QUEUE}
