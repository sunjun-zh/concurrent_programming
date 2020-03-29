# -*-coding:utf-8-*-
import queue
from threading import Thread, currentThread


def producer(out_q, n):
    print(f'{currentThread().getName()} put data in queue')
    [out_q.put(i) for i in range(n)]


def consumer(in_q):
    while True:
        data = in_q.get()
        print(f'{currentThread().getName()} get data: {data}')
        in_q.task_done()


if __name__ == '__main__':
    q = queue.Queue()

    t1 = Thread(target=producer, args=(q, 6))
    t2 = Thread(target=consumer, args=(q, ), daemon=True)

    t1.start()
    t2.start()

    q.join()