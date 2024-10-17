from threading import Thread
from datetime import datetime
import time

def current_time(who):
    time.sleep(1)
    print(f"{who} is running")
    print(datetime.now())

current_time("Main thread")

t1 = Thread(target=current_time, args=["t1"])
t2 = Thread(target=current_time, args=["t2"])
t3 = Thread(target=current_time, args=["t3"])
t4 = Thread(target=current_time, args=["t4"])

t1.start()
t2.start()
t3.start()
t4.start()
print("All threads started")
t1.join()
t2.join()
t3.join()
t4.join()
print("All threads are finished")