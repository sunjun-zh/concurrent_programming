# -*-coding:utf-8-*-
import gevent
from gevent import Timeout


def task():
    gevent.sleep(2)
    print(f'task {gevent.getcurrent()} done')


def test1():
    timeout = Timeout(10)  # constrain executing greenlet
    timeout.start()

    try:
        gevent.spawn(task).join()
    except Timeout:
        print('could not complete')


def test2():
    timer = Timeout.start_new(3)  # constrain executing greenlet
    thread = gevent.spawn(task)
    try:
        thread.get(timeout=timer)
    except Timeout:
        print('could not complete')


if __name__ == '__main__':
    # test1()
    test2()
