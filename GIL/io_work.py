# -*-coding:utf-8-*-
import time
from multiprocessing import Process
from threading import Thread


def task():
    time.sleep(2)


if __name__ == '__main__':
   l= []

   start = time.time()
   for i in range(1000):
       # p = Process(target=task) # 5.496253728866577
       p = Thread(target=task) # 2.0723578929901123
       l.append(p)
       p.start()

   for p in l:
       p.join()

   end = time.time()
   print(f'run time:: {end-start}')

# multithread is better than multiprocess