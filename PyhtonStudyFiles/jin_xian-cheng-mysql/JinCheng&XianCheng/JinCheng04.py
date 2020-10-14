# import queue
#
#
# # 创建一个队列
# q = queue.Queue()  # 括号内传数字，表示生成的队列可以同时存放的数据

'''
队列：先进先出
堆栈：先进后出
管道：subprocess,stdin,stdout,stderr
队列 = 管道 + 锁

'''

from multiprocessing import Queue
q = Queue(5)

'''
存超了，取超了都会原地阻塞 q.put，q.get
q.get(timeout=数字) 等待数字秒后报错queue.Empty
q.get_nowait()  没有数据直接报错queue.Empty    多进程下不准确
q.full() 判断当前队列是否满了                  多进程下不准确
q.empty() 判断当前队列是否空了                 多进程下不准确
'''
