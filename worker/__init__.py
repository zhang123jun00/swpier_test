import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTING_MODULE", "swiper.settings")

# 创建Celery 应用
celery_app = Celery('swiper')
celery_app.config_from_object('work.config')
celery_app.autodiscover_tasks()

def call_by_worker(func):
    '''将任务在Celery中异步执行'''
    task = celery_app.task(func)
    return task.delay
