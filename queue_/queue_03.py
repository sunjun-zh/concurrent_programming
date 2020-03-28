# -*-coding:utf-8-*-
import time
import queue

q = queue.PriorityQueue(3) # priority level

def task():
    # q.put((time.time(), 'a'))
    # q.put((time.time(), 'b'))
    # q.put((time.time(), 'c'))
    #
    q.put((2, 'a'))
    q.put((1, 'b'))
    q.put((6, 'c'))


    time.sleep(1)

    print(q.get())
    print(q.get())
    print(q.get())


if __name__ == '__main__':
    task()



