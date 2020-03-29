# -*-coding:utf-8-*-

import gevent
from gevent import monkey


def test():
    import socket
    print(socket.socket)

    monkey.patch_all()
    print(socket.socket)


if __name__ == '__main__':
    test()
