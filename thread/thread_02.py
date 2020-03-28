# -*-coding:utf-8-*-
import time
from threading import Thread


class Customize_Thread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'{self.name} is running')
        time.sleep(1)
        print(f'{self.name} is done')


if __name__ == '__main__':
    t = Customize_Thread(name='zh')
    t.start()
    # t.join()

    print('main thread')
