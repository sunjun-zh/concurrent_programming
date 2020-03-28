# -*-coding:utf-8-*-
import time
from multiprocessing import Process, Queue

q = Queue(3)

def task(name, i, q):
    print(f'{name} is running')
    time.sleep(1)
    q.put(i)  # process will block if q is full and q still pull sth
    if q.full():
        print('queue_ if full')
    print(f'{name} is done')


if __name__ == '__main__':
    for i in range(6):
        p = Process(target=task, args=(f'zh-{i}',i, q))
        p.start()

    print('main process')
