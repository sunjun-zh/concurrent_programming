# -*-coding:utf-8-*-
import time
from threading import Thread, Event, currentThread

# event.isSet()  #return event'status
# event.wait()  # if event.isSet==False, threat will be block
# event.set()  # set event'status True
# event.clear()  # set event'status False


event = Event()


def conn():
    n = 0
    while not event.is_set():
        if n == 3:
            print(f'{currentThread().getName()} try too many times')
            return
        print(f'{currentThread().getName()} try {n}')
        event.wait(0.5)
        n += 1


def check():
    print(f'{currentThread().getName()} is checking')
    time.sleep(2)
    event.set()
    print(f"{currentThread().getName()} check over")


if __name__ == '__main__':
    for i in range(3):
        x = Thread(target=conn)
        x.start()

    t = Thread(target=check)
    t.start()
