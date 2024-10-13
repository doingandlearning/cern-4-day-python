from threading import Thread, Timer
from time import sleep
from random import randint


def printer(msg, max_sleep):
    for _ in range(0, 10):
        time_to_sleep = randint(1, max_sleep)
        sleep(time_to_sleep)
        print(msg, end='')


def print_arrow():
    print('-->')
    t = Timer(5, print_arrow)
    t.start()


def main():
    t1 = Thread(target=printer, args=('A', 10))
    t2 = Thread(target=printer, args=('B', 5))
    t3 = Thread(target=printer, args=('C', 15))
    t4 = Thread(target=printer, args=('D', 7))
    t5 = Thread(target=printer, args=('E', 2))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    # Extension point
    t = Timer(5, print_arrow)
    t.start()


if __name__ == "__main__":
    main()
