# -*-coding:utf-8-*-
import time
from multiprocessing import Process, JoinableQueue


# producer<-->queue<-->customer

def producer(name, q):
    print(f'{name} start to produce sth')
    time.sleep(1)
    [q.put(name+'-'+str(k)) for k in range(1)]
    # [q.put(None) for k in range(2)]
    print(f'{name} is done')
    q.join() # waiting customer consuming product


def customer(name, q):
    print(f'{name} start to consume sth')
    while True:
        sth = q.get()
        # if sth is None: break
        time.sleep(1)
        print(f'{name} is consuming {sth}')
        q.task_done() # send a msg to tell producer



if __name__ == '__main__':
    q = JoinableQueue()
    # for i in range(2):
    p1 = Process(target=producer, args=(f'producer-1', q))
    p2 = Process(target=producer, args=(f'producer-2', q))
    p3 = Process(target=producer, args=(f'producer-3', q))
    c1 = Process(target=customer, args=(f'customer-{1}', q))
    c2 = Process(target=customer, args=(f'customer-{2}', q))
    c1.daemon =True  # if not setting daemon, the customer-subprocess will block forever
    c2.daemon =True

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()


    print('main process')
