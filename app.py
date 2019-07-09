import datetime
import os
import pytz
from setting import *
import rainfall
import push
from apscheduler.schedulers.blocking import BlockingScheduler


timezone = os.getenv('TIMEZONE')
hour_of_day = os.getenv('HOUR_OF_DAY')


def send_rainfall():
    now = datetime.datetime.now(pytz.timezone(timezone))
    dt_str = now.strftime('%Y-%m-%d %H:%M')
    print(f'starting app at {dt_str}')
    title = f'Rainfall ({dt_str})'
    result = rainfall.calculate()
    push.send_to_device(title, result)


scheduler = BlockingScheduler(timezone=timezone)


@scheduler.scheduled_job('interval', minutes=3)
def job():
    send_rainfall()


@scheduler.scheduled_job('cron', hour=hour_of_day)
def scheduled_job():
    send_rainfall()


scheduler.start()
