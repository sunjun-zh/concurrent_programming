# -*-coding:utf-8-*-
import time
import queue

q = queue.LifoQueue(3) # last in first out

def task():
    q.put('a')
    q.put('b')
    q.put('c')

    time.sleep(1)

    print(q.get())
    print(q.get())
    print(q.get())


if __name__ == '__main__':
    task()



