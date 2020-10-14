from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time


pool1 = ThreadPoolExecutor(5) # 线程池中固定只有5个线程
# 括号内传入数字
'''
池子造出来之后  里面固定存在五个线程
这五个线程不会出现重复创建和销毁的情况

池子的使用，仅仅需要向任务池子中提交任务即可,池子自动服务
'''

def task(n):
    print(n)
    time.sleep(2)
    return n, 'ok'

'''
任务的提交方式：同步/异步
pool1.submit(task, 1)
print('main') # submit是异步提交
'''

list_this = []
for i in range(20):
    res = pool1.submit(task, i)
    # print(res.result()) # 程序由并发变成了串行，res.result()为目标程序的返回结果
    list_this.append(res)

pool1.shutdown()  # 关闭线程池，等待线程池中的所有任务运行完毕

for this in list_this:
    print(this.result())



