# -*-coding:utf-8-*-
import time
from threading import Thread, Event
from multiprocessing import Process


def countdown(n, event):
    print(f"countdown starting; event'status: {event.isSet()}")
    event.set()
    while n > 0:
        print(f'T-minus {n}')
        n -= 1
        time.sleep(2)


if __name__ == '__main__':
    e = Event()
    t = Thread(target=countdown, args=(5, e))
    t.start()

    e.wait() # countdown is always running util countdown starting
    print('countdown is running')
