# -*-coding:utf-8-*-
import queue
from threading import Thread, Event


class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = queue.Queue()

    def sent(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.sent(ActorExit)

    def start(self):
        self._terminal = Event()
        t = Thread(target=self._bootstrap, daemon=True)
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminal.set()

    def join(self):
        self._terminal.wait()

    def run(self):
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print(f'got: {msg}')


class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'do_' + tag)(*payload)

    def do_A(self, x):
        print(f'running a: {x}')

    def do_B(self, x, y):
        print(f'running a: {x} {y}')


class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.sent((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


def test1():
    p = PrintActor()
    p.start()

    p.sent('hello world')
    p.sent('hi, friends')

    p.close()
    p.join()


def test2():
    p = PrintActor()
    p.start()

    p.sent(('A', 1))
    p.sent(('B', 2, 3))

    p.close()
    p.join()


def test3():
    w = Worker()
    w.start()
    r = w.submit(pow, 2, 3)
    print(r.result())


if __name__ == '__main__':
    # test1()
    # test2()
    test3()
    print('main')
