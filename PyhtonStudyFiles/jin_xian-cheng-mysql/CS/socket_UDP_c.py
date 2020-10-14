from socket import *

ip_port = ('127.1.0.2', 8456)
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('请输入您想发送给服务端的消息:').strip()
    udp_client.sendto(data.encode('utf-8'), ip_port)

    msg, addr = udp_client.recvfrom(buffer_size)
    print('从服务端收到的消息为：', msg.decode('utf-8'))
