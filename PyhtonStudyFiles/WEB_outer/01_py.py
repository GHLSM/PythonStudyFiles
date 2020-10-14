from socket import *


server = socket()
server.bind(('127.0.0.1', 8080))
server.listen(5)


while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    print(data)
    # 直接忽略favicon.ico
    data = data.decode('utf-8')
    # 获取字符串中特定的内容  正则/切割（字符串有规律）
    current_path = data.split(' ')[1]
    # print(current_path)
    if current_path == '/index':
        with open(r'01_html.html', 'rb') as f:
            conn.send(f.read())
    conn.send(b'hello')
    conn.close()
    # 不足之处：代码重复，并发问题，获取信息不全很少
