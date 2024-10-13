import threading
from threading import Thread

from worker import worker

t1 = Thread(name='worker', target=worker, args='A')
t2 = Thread(target=worker, args='B')  # use default name e.g. Thread-1
d = Thread(daemon=True, name='daemon', target=worker, args='C')

t1.start()
t2.start()
d.start()

print()
for t in threading.enumerate():
    print(t.name)
