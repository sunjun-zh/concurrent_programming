# -*-coding:utf-8-*-

def countdown(n):
    while n > 0:
        print(f'T-minus: {n}')
        yield  # Suspend its execution
        n -= 1
    print('blastoff')


def countup(n):
    x = 0
    while x < n:
        print(f'counting up {x}')
        yield
        x += 1


if __name__ == '__main__':
    for i in countdown(10):
        pass

    for i in countup(10):
        pass
