import socket
import select


server = socket.socket()
server.bind(('127.0.0.1', 8945))
server.listen(5)
server.setblocking(False)
read_list = [server]
'''帮助监管
一旦有连接来了，立马将对象返回给你'''
while True:
    r_list, w_list, x_list  = select.select(read_list, [], [])
    for i in r_list:
        if i is server:
            conn, addr = i.accept()
            # 将conn添加到监管机制中
            read_list.append(conn)
        else:
            res = i.recv(1024)
            if res:
                i.close()
            read_list.remove(i)
            continue
            print(res)
            i.send(b'hi')
