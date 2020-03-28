# -*-coding:utf-8-*-
import random
from threading import Timer, currentThread


class Code():
    def __init__(self):
        self.make_cache()

    def make_cache(self, interval=5):
        self.cache = self.make_code()
        print(f'{currentThread().getName()} generate a cache: {self.cache}')
        self.t = Timer(interval, self.make_cache)
        self.t.start()

    def make_code(self, length=6):
        code = ''
        for i in range(length):
            a = str(random.randint(0, 9))
            b = chr(random.randint(65, 90))
            code += random.choice([a, b])
        return code

    def check(self):
        while True:
            code = input('please input your cache code:').strip()
            if code.upper() == self.cache:
                self.t.cancel()
                break


if __name__ == '__main__':
    c = Code() # first stop: generate cache code
    c.check()
