# -*-coding:utf-8-*-
import gevent
from gevent.pool import Pool
from gevent.lock import BoundedSemaphore
from gevent.queue import Queue, Empty

mutex = BoundedSemaphore(2)


def worker1(n):
    mutex.acquire()
    print(f'worker1-{n}({gevent.getcurrent()}) acquired semaphore')
    # gevent.sleep(0.5)
    mutex.release()
    print(f'worker1-{n}({gevent.getcurrent()}) released semaphore')




def worker2(n):
    with mutex:
        print(f'worker2-{n}({gevent.getcurrent()}) acquired semaphore')
        # gevent.sleep(1)
    print(f'worker2-{n}({gevent.getcurrent()}) released semaphore')


if __name__ == '__main__':
    p = Pool()
    p.map(worker1, range(3))
    p.map(worker2, range(5))
