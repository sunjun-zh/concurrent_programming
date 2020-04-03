# -*-coding:utf-8-*-
import gevent


def say_hi():
    print(f'running in say_hi {gevent.getcurrent().name}')
    gevent.sleep(1)
    print(f'context switch to say_hi again {gevent.getcurrent()}')


def do_work():
    print(f'running in do_work {gevent.getcurrent()}')
    gevent.sleep(2)
    print(f'context switch to do_work again {gevent.getcurrent()}')


if __name__ == '__main__':
    # gevent.spawn(say_hi).run()

    # gevent.joinall([gevent.spawn(say_hi), gevent.spawn(do_work), ])
    gevent.spawn(say_hi)
    while 1:
        print(gevent.getcurrent())
        gevent.sleep(10)
        # break
