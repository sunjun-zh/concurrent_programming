# -*-coding:utf-8-*-
import time
from threading import Thread, Event

# event.isSet()  #return event'status
# event.wait()  # if event.isSet==False, threat will be block
# event.set()  # set event'status True
# event.clear()  # set event'status False


event = Event()


def student(name):
    start = time.time()
    print(f'{name} is listening class')
    print(f'{name} (before)event-status::{event.is_set()}')
    event.wait() # if dont set time，the thread will be block util event'status change
    end = time.time()

    print(f'{name} (after)event-status::{event.is_set()} {end - start}')
    print(f'{name} attend an in-class activities')


def teacher(name):
    print(f'{name} is teaching')
    time.sleep(10)
    event.set()
    print(f"{name}'s lesson over")


if __name__ == '__main__':
    x = Thread(target=student, args=('x',))
    y = Thread(target=student, args=('y',))
    z = Thread(target=student, args=('z',))
    t = Thread(target=teacher, args=('t',))

    x.start()
    y.start()
    z.start()
    t.start()
