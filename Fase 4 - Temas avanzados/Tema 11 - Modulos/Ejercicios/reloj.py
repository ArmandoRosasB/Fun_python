import datetime
import time
import os

dt = datetime.datetime.now()
t = datetime.timedelta(seconds= 1)
while True:
    os.system('cls')
    print(dt.strftime("%H: %M: %S"))
    dt = dt + t
    time.sleep(1)