# -*-coding:utf-8-*-
import os
import time
from multiprocessing import Process



class Customize_process(Process):
    def __init__(self, name):
        super().__init__()  # inherit parent init-function
        self.name = name

    def run(self):
        # os.getpid() subprocess_id
        # os.getppid() parent_id
        print(f'{self.name}({os.getpid()}) is running')
        time.sleep(1)
        print(f'{self.name} is done')


if __name__ == '__main__':
    p = Customize_process('zh')
    p.run()
    print(p.pid)
    print(f'main {os.getppid()}')