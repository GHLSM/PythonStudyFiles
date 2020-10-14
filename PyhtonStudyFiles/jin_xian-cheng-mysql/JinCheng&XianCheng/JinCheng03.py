'''
互斥锁：将并发变为串行，保持数据的安全,牺牲效率
           不同进程对同一份数据进行处理时
          1.不要轻易用锁。容易造成死锁现象
          2.仅在处理数据时加上锁
'''
from multiprocessing import Process
from multiprocessing import Lock
import time
import json
import random
def searth_tic(name):
    with open('ticket_num', 'r', encoding='utf-8') as f:
        data_dic = json.load(f)
    print('%s 查询剩余票数为 %s' % (name, data_dic.get('tic_num')))

def buy(name):
    with open('ticket_num', 'r', encoding='utf-8') as f:
        data_dic = json.load(f)
    time.sleep(random.randint(1, 3))

    if data_dic.get('tic_num') > 0:
        data_dic['tic_num'] -= 1
        with open('ticket_num', 'w', encoding='utf-8') as f:
            json.dump(data_dic, f)
        print('%s success' % name)
    else:
        print('%s false' % name)
def run(name, mutex):
    searth_tic(name)
    # buy环节加锁处理，枪锁
    mutex.acquire()
    buy(name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for name in range(1, 10):
        P = Process(target=run, args=(name, mutex))
        P.start()
