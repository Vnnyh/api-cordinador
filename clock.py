import requests
import json
import base64
from apscheduler.schedulers.blocking import BlockingScheduler
import api_request from hotel

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=60)
def timed_job():
    api_request()

sched.start()
