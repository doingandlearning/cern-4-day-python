from multiprocessing import Process, set_start_method
import os


def worker(msg):
    print(f'process id: {os.getpid()}')
    for _ in range(0, 10):
        print(msg, end='', flush=True)


if __name__ == '__main__':
    set_start_method('spawn')
    print('Starting')
    print(f'Root application process id: {os.getpid()}')

    p2 = Process(target=worker, args='A')
    p3 = Process(target=worker, args='B')
    p4 = Process(target=worker, args='C')

    p2.start()
    p3.start()
    p4.start()

    print('Done')
