from setting import *
import rainfall
import push


result = rainfall.calculate()
push.send_to_device(result)
