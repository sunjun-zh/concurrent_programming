# -*-coding:utf-8-*-
import time
import json
from multiprocessing import Process, Lock


def search_count(name):
    result = json.load(open('../data/tickets.json', 'r')) #dict
    print(f'{name} watch the remaining tickets: {result["count"]}')


def get_ticket(name):
    time.sleep(1)
    result = json.load(open('../data/tickets.json', 'r')) #dict
    if result['count']>0:
        result['count'] -= 1
        time.sleep(2)
        json.dump(result, open('../data/tickets.json', 'w'))
        print(f'{name} buy ticket success')
    else:
        print(f'{name} buy ticket fail')


def task(name, mutex):
    # print(f'{name} is running')
    search_count(name)
    mutex.acquire()
    get_ticket(name)
    print(f'{name} is done')
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    # mutex = None
    for i in range(6):
        p = Process(target=task, args=(f'zh-{i}', mutex))  # transport mutex-lock to make work in a certain order
        p.start()
        # p.join()

    print(f'main process')
