# -*-coding:utf-8-*-
import gevent
from gevent.local import local

local_data = local()


def f1():
    local_data.x = 1
    print(f'({gevent.getcurrent()}) set value: {local_data.x}')


def f2():
    local_data.y = 2
    print(f'({gevent.getcurrent()}) set value: {local_data.y}')

    try:
        gevent.sleep(1)
        local_data.x
    except AttributeError:
        print('x is not local to f2')


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(f1),
        gevent.spawn(f2),
    ])
