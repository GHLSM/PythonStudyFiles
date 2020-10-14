from socket import *
import struct
# from functools import partial

ip_port = ('127.1.0.3', 8456)
back_log = 5
buffer_size = 1024
place = 'gbk'

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    cmd = input('>>:').strip()
    if not cmd:
        continue
    if cmd == 'quit':
        break
    tcp_client.send(cmd.encode('utf-8'))

    # low的解决方式
    # length = tcp_client.recv(buffer_size)  # 接收服务端发过来的数据长度
    # tcp_client.send(b'ready')
    # length = int(length.decode('utf-8'))
    # recv_size = 0
    # recv_msg = b''
    # while recv_size < length:
    #     recv_msg += tcp_client.recv(buffer_size)
    #     recv_size = len(recv_msg)

    length_data = tcp_client.recv(4)  # 接收服务端发过来的数据长度
    length = struct.unpack('i', length_data)[0]

    # recv_msg = ''.join(iter(partial(tcp_client.recv, buffer_size), b''))
    # print('处理结果为', recv_msg)

    recv_size = 0
    recv_msg = b''
    while recv_size < length:
        recv_msg += tcp_client.recv(buffer_size)
        recv_size = len(recv_msg)
    print('处理结果为', recv_msg.decode('gbk'))

tcp_client.close()
