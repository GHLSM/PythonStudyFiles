from threading import Thread

money = 100
def task():
    global money
    money = 666
    print(money)

if __name__ == '__main__':
    t = Thread(target=task)
    t.start()
    print(money)