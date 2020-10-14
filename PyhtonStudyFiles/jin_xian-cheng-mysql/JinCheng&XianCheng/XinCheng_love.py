import time
from threading import Thread


def task(name):
    print('%s is running' % name)
    time.sleep(1)
    print('%s is over' % name)

if __name__ == '__main__':
    t = Thread(target=task, args=('alex',))
    t.daemon = True
    t.start()
    print('main')

'''
主线程结束之后不会立即结束，
    会等待所有其他非守护线程结束之后才会结束
主线程结束意味着空间回收

'''