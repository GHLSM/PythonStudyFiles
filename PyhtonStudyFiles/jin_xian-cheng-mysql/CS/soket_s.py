import socket
ip_port = ('127.1.0.2', 8456)
back_log = 5
buffer_size = 1024

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(ip_port)

phone.listen(back_log)  #最大挂起链接数  ##backlog的概念

conn, addr = phone.accept()  #返回元组信息(conn, addr)

data = conn.recv(buffer_size)
conn.send(data)

conn.close()
phone.close()
