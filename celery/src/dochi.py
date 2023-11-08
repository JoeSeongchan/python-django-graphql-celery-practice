# dochi.py
import time
import random

from celery import Celery

# 첫번째 인자 : Celery 이름
# broker = RabbitMQ
app = Celery('tasks', broker='amqp://cho:cho@localhost:5672//')


@app.task # Task 설정
def working(id=1):
    # 1~5초 사이의 랜덤한 Delay를 발생.
    time.sleep(random.randint(1, 5))

    return '{}번째, 일을 끝냈다.'.format(id)