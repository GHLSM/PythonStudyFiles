from threading import Thread
from threading import Event
import time
import random


event = Event()
def light():
    print('红灯亮')
    time.sleep(random.randint(3,5))
    print('绿灯亮了')
    event.set() #告诉wait方法可以继续执行

def car(name):
    print('%s waiting' % name)
    event.wait()  # 等待事件消息
    print('%s run' % name)

if __name__ == '__main__':
    t = Thread(target=light)
    t.start()
    for i in range(20):
        ca = Thread(target=car, args=(i,))
        ca.start()