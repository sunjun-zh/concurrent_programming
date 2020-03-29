# -*-coding:utf-8-*-
from collections import deque


class ActorScheduler:
    def __init__(self):
        self._actors = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._msg_queue.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass



if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print(f'got: {msg}')

    def counter(s):
        while True:
            n = yield
            if n==0:
                break
            s.send('printer', n)
            s.send('counter', n-1)

    s = ActorScheduler()
    s.new_actor('printer', printer())
    s.new_actor('counter', counter(s))

    s.send('counter', 100)
    s.run()