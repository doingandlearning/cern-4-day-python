from multiprocessing import Process, set_start_method


def worker(msg):
    for _ in range(0, 10):
        print(msg, end='', flush=True)


if __name__ == '__main__':
    print('Starting')
    set_start_method('spawn')
    t = Process(target=worker, args='A')
    t.start()
    print('Done')
