# -*-coding:utf-8-*-
import time
from multiprocessing import Process, Queue


# producer<-->queue_<-->customer

def producer(name, q):
    # print(f'{name} start to produce sth')
    [q.put(name+'-'+str(k)) for k in range(1)]
    [q.put(None) for k in range(2)]
    print(f'{name} is done')


def customer(name, q):
    print(f'{name} start to consume sth')
    while True:
        sth = q.get()
        if sth is None: break
        time.sleep(1)
        print(f'{name} is consuming {sth}')



if __name__ == '__main__':
    q = Queue()
    for i in range(2):
        p = Process(target=producer, args=(f'producer-{i}', q))
        p.start()
        p.join()

    for i in range(3):
        p = Process(target=customer, args=(f'customer-{i}', q))
        p.start()

    print('main process')
