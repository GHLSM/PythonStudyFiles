from multiprocessing import Process
from multiprocessing import current_process
import time
import os


# #查看当前进程进程号
def task():
    # print('%s id running' % current_process().pid)
    print('%s id running' % os.getpid())
    # print('%s id running' % os.getppid())
    time.sleep(3)


if __name__ == '__main__':
    P = Process(target=task)
    P.daemon = True  # 设置为P守护进程，必须在start前面
    P.start()
    print('main')
    P.terminate() # 杀死当前进程
    print(P.is_alive()) # p判断当前进程是否存活

# current_process().pid  查看当前进程进程号
# os.getpid 查看当前进程进程号
# os.getppid 查看父进程的pod号
