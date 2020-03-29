# -*-coding:utf-8-*-
import gevent
from gevent.queue import Queue

q = Queue()


def producer(name):
    print(f'producer({name}) is running')
    while not q.empty():
        task = q.get()
        print(f'producer({name}) get task: {task}')
        gevent.sleep(1)


def customer():
    print(f'customer({gevent.getcurrent()}) is running')
    for i in range(10):
        q.put_nowait(i)


if __name__ == '__main__':
    gevent.spawn(customer).join()

    gevent.joinall([
        gevent.spawn(producer, 'a'),
        gevent.spawn(producer, 'b'),
        gevent.spawn(producer, 'c'),
    ])
