from  threading import Thread
# import os
import time


def task():
    print('hello')
    # print('hello world', current_thread().name)  # 获得当前进程的名称

if __name__ == '__main__':
    t = Thread(target=task)
    t.start()
    print('main')

'''  
  print('main',os.getpid()) # 获得进程号
  print('main', active_count()) # 统计活跃的线程数
'''