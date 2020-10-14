# 利用IPC机制，队列解决进程数据通信问题

from multiprocessing import Queue, Process


def producer(q):
    q.put('hi')
    print('hello big baby')

def consumer(q):
    q.get()
    print('get you')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p.start()
    p2.start()
    # data_q = q.get()
    # print(data_q)
