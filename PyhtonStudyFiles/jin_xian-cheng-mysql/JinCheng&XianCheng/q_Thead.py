'''同一个进程下的多个线程数据是共享的
队列 = 管道 + 锁
保护用户数据安全'''

import queue
# 使用的队列都只能在本地测试使用，做项目时几乎不用

# 队列q ：先进先出
q1 = queue.Queue(3)

# q ：后进先出
q2 = queue.LifoQueue(3) #last in first out Queue

# 优先q  可以给放入队列中的数据设置优先级
q3 = queue.PriorityQueue(3)
q3.put((3, '111'))
q3.put((-5, '111'))
q3.put((0, '111'))
print(q3.get())  # 数字越小，优先级越高

