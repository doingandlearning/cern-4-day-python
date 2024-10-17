from threading import Thread
import time
import random

def read_sensor_data(queue):
    while True:
        data = random.random()
        queue.append(data)
        time.sleep(0.1)

data_queue = []
thread1 = Thread(target=read_sensor_data, args=[data_queue])
thread1.start()


def process_data(queue):
    while True:
        if queue:
            data = queue.pop(0)
            print(f"Processing: {data}")
        time.sleep(0.5)

thread2 = Thread(target=process_data, args=[data_queue])
thread2.start()