import datetime
import os
import pytz
from setting import *
import rainfall
import push
from cron_descriptor import get_description
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

timezone = os.getenv('TIMEZONE')
crontab = os.getenv('CRONTAB')
crontab_desc = get_description(crontab)


def send_rainfall():
    now = datetime.datetime.now(pytz.timezone(timezone))
    dt_str = now.strftime('%Y-%m-%d %H:%M')
    print(f'starting app at {dt_str}')
    title = f'Rainfall ({dt_str})'
    result = rainfall.calculate()
    push.send_to_device(title, result)


scheduler = BlockingScheduler()
scheduler.add_job(send_rainfall, CronTrigger.from_crontab(crontab, timezone=timezone))
print(f'scheduled job to run {crontab_desc}')
scheduler.start()
