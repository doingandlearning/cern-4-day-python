from threading import Thread
from time import sleep


def worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


def worker2(prompt, message):
    for i in range(0, 10):
        print(prompt, message, end='', sep='', flush=True)
        sleep(1)


print('Starting')
t1 = Thread(target=worker, args='A')
t2 = Thread(target=worker, args='B')
t3 = Thread(target=worker, args='C')
t4 = Thread(target=worker2, args=('D', 'E'))
t1.start()
t2.start()
t3.start()
t4.start()

print('Done')
