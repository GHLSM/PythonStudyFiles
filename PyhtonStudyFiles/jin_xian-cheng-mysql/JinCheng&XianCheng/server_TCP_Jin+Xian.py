from socket import *
from threading import Thread
from multiprocessing import Process
"""
服务端
    1.固定IP&PORT
    2.不间断服务
    3.支持并发
"""
buffsize = 1024
server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8945,))
server.listen(5)

def server_talk(conn):
    while True:
        try:
            data = conn.recv(buffsize)
            if not data:
                break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break
    conn.close()

while True:
    conn, addr = server.accept()
    # 通讯循环
    t = Thread(target=server_talk, args=(conn, ))
    t.start()






