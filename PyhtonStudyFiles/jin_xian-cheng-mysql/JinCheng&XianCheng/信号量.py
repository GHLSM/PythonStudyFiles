from threading import Thread
from threading import Semaphore
import time
import random


sm = Semaphore(5)  # 锁的个数
def task(name):
    sm.acquire()
    print('%s is get' % name)
    time.sleep(random.randint(1,5))
    sm.release()

if __name__ == '__main__':
    for i in range(20):
        t = Thread(target= task, args=('%s' % i,))
        t.start()