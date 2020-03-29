# -*-coding:utf-8-*-
import gevent
from gevent.queue import Queue, Empty

q = Queue()


def producer(name):
    print(f'producer({name}) is running')
    try:
        while not q.empty():
            task = q.get()
            print(f'producer({name}) get task: {task}')
            gevent.sleep(0.01)
    except Empty:
        print(f'producer({name}) quit')


def customer():
    print(f'customer({gevent.getcurrent()}) is running')
    for i in range(100):
        q.put_nowait(i)

    for i in range(100, 200):
        q.put_nowait(i)


if __name__ == '__main__':

    gevent.joinall([
        gevent.spawn(customer),
        gevent.spawn(producer, 'a'),
        gevent.spawn(producer, 'b'),
        gevent.spawn(producer, 'c'),
    ])
