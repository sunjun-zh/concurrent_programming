# -*-coding:utf-8-*-
import time
from multiprocessing import Process
from threading import Thread


def task():
    res = 1
    for i in range(1000000):
        res += i



if __name__ == '__main__':
   l= []

   start = time.time()
   for i in range(1000):
       p = Process(target=task) # 18.184703826904297
       # p = Thread(target=task) # 55.30943322181702
       l.append(p)
       p.start()

   for p in l:
       p.join()

   end = time.time()
   print(f'run time:: {end-start}')

#  multiprocess is better than multithread