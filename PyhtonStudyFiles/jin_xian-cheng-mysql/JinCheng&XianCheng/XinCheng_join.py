from threading import Thread
import time



def task(name):
    print('%s is running' % name)
    time.sleep(1)
    print('%s is over' % name)

if __name__ == '__main__':
    t = Thread(target=task, args=('alex', ))
    t.start()
    t.join() # 主线程等待子线程结束再执行
    print('main')

