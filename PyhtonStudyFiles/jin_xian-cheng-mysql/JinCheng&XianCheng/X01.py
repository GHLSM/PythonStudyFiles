from multiprocessing import Process
from threading import Thread
import os
import time

def work():
    res = 1
    for i in range(1,10000000):
        res *= 1

if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 获取当前CPU个数
    start_time = time.time()
    for i in range(os.cpu_count()):
        # p = Process(target= work)
        p = Thread (target= work)
        p.start()
        l.append(p)
    
    for p in l:
        p.join()
    print(time.time() - start_time)