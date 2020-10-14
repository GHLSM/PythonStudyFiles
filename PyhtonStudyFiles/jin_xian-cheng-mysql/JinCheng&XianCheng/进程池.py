from concurrent.futures import ProcessPoolExecutor
import time
import os


pool1 = ProcessPoolExecutor(5) # 线程池中固定只有5个进程
# 括号内传入数字
'''
池子造出来之后  里面固定存在五个进程
这五个进程不会出现重复创建和销毁的情况

池子的使用，仅仅需要向任务池子中提交任务即可,池子自动服务
'''

def task(n):
    print(n, os.getpid())
    time.sleep(2)
    return n, 'ok'

'''
任务的提交方式：同步/异步
    同步: 提交任务之后原地等待任务返回结果，不做任何事
    异步：不等待，继续执行
        异步反馈结果获取，应该通过回调机制解决
    回调机制：相当于每个异步任务绑定定时炸弹
                一旦任务有结果立即触发



pool1.submit(task, 1)
print('main') # submit是异步提交
'''

def call_back(n):
    print(n.result())

if __name__ == '__main__':
    list_this = []
    for i in range(20):
        # res = pool1.submit(task, i)
        res = pool1.submit(task, i).add_done_callback(call_back) # 添加的回调机制
        # print(res.result()) # 程序由并发变成了串行，res.result()为目标程序的返回结果
        # list_this.append(res)

    # pool1.shutdown()  # 关闭进程池，等待进程池中的所有任务运行完毕
    #
    # for this in list_this:
    #     print(this.result())


