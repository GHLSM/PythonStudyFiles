import socket
ip_port = ('127.1.0.2', 8456)
back_log = 5
buffer_size = 1024
data = 'data'

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(ip_port)
phone.send(data.encode('utf-8'))
phone.recv(buffer_size)

phone.close()


