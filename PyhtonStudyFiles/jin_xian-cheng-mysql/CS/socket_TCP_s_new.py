from socket import *
ip_port = ('127.1.0.3', 8456)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   # 服务器重启时重用ip地址
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:
    print('服务端开始接受消息')
    conn, addr = tcp_server.accept()

    print('双向链接是', conn)
    print('客户端地址是', addr)

    while True:
        try:
            data = conn.recv(buffer_size)
            # if not data:break  ##mac中不报异常的死循环解决方式
            print('客户端发来的消息是', data.decode('utf-8'))
            conn.send(data.upper())
        except Exception:
            break
    conn.close()

# tcp_server.close()
