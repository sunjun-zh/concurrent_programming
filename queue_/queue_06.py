# -*-coding:utf-8-*-
import queue
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def echo_client(q):
    sock, client_addr = q.get()
    print(f'got connection from {client_addr}')
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('client closed connection')
    sock.close()


def echo_server(addr, nworkers):
    q = queue.Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,), daemon=True)
        t.start()

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)

    while True:
        client_sock, client_addr = sock.accept()
        q.put(client_sock, client_addr)


if __name__ == '__main__':
    echo_server(('', 15000), 128)
