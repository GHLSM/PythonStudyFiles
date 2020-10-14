# 开启线程的两种方式
import time
from threading import Thread


def task(name):
    print('%s is running' % name)
    time.sleep(1)
    print('%s is over' % name)


'''
开启线程不需要在main下面执行代码，直接书写
但是我们习惯性还是将启动命令写在main下面
'''
if __name__ == '__main__':
    t = Thread(target=task, args=('alex',))
    t.start()
    print('main')


class MyThead(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def run(self) -> None:
        print('hello')
        time.sleep(3)
        print('out')


if __name__ == '__main__':
    p = MyThead('alex')
    p.start()
    print('main')

