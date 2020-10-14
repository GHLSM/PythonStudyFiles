from multiprocessing import Process
import time


def task(name):
    print('%s is running' % name)
    time.sleep(3)
    print('%s is over' % name)


'''
windoes操作系统下  创建进程一定要在main内创建
    因为windows下创建进程类似于模块导入的模式
    会从上往下依次执行代码
linux直接将代码拷贝一份
'''

if __name__ == '__main__':
    p1 = Process(target=task, args=('json',))  # 创建对象
    p2 = Process(target=task, args=('egon',))  # 创建对象
    p3 = Process(target=task, args=('tank',))  # 创建对象
    p1.start()  # 开启进程
    p2.start()  # 开启进程
    p3.start()  # 开启进程
    # p.join() # 主进程等待子进程运行结束之后再继续执行
    print('main is running over')

# 类的继承也可以开启进程
class MyProcess(Process):
    def run(self) -> None:
        print('hello')
        time.sleep(3)
        print('out')


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('main')

