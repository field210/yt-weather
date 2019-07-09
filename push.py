from pushbullet import Pushbullet
import os
from setting import *


def send_to_device(title, body):
    # push result to device
    api_key = os.getenv('PUSHBULLET_API')
    pb = Pushbullet(api_key)
    push = pb.push_note(title, body)

    return
