# from socket import *
# import subprocess
#
# ip_port = ('127.1.0.3', 8456)
# back_log = 5
# buffer_size = 1024
# place = 'gbk'
#
# tcp_server = socket(AF_INET, SOCK_STREAM)
# tcp_server.bind(ip_port)
# tcp_server.listen(back_log)
#
# while True:
#     conn, addr = tcp_server.accept()
#     print('新的客户链接为', addr)
#     while True:
#         try:
#             cmd = conn.recv(buffer_size)
#             if not cmd:
#                 break
#
#             print('收到用户的命令为', cmd)
#
#             res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
#                                    stderr= subprocess.PIPE,
#                                    stdout= subprocess.PIPE,
#                                    stdin= subprocess.PIPE)
#
#             err = res.stderr.read()
#             if err:
#                 com_res = err
#             else:
#                 com_res = res.stdout.read()
#             if not com_res:
#                 com_res = '执行成功，但无返回值'
#                 com_res.encode(place)
#             conn.send(com_res)
#         except Exception as e:
#             print(e)
#             break

# ####粘包问题解决
from socket import *
import subprocess
import struct

ip_port = ('127.1.0.3', 8456)
back_log = 5
buffer_size = 1024
place = 'gbk'

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:
    conn, addr = tcp_server.accept()
    print('新的客户链接为', addr)
    while True:
        try:
            cmd = conn.recv(buffer_size)
            if not cmd:
                break

            print('收到用户的命令为', cmd)

            res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)

            err = res.stderr.read()
            if err:
                com_res = err
            else:
                com_res = res.stdout.read()
            if not com_res:
                com_res = '执行成功，但无返回值'
                com_res.encode(place)

            # low的解决方式
            # com_res_len = len(com_res)
            # conn.send('com_res_len'.encode('utf-8'))
            # tcp_server_ready = conn.recv(buffer_size)
            # if tcp_server_ready == b'ready':
            #     conn.send(com_res)

            com_res_len = len(com_res)
            data_length = struct.pack('i', com_res_len)
            # conn.send(data_length)
            # conn.send(com_res)
            conn.sendall(data_length+com_res)
        except Exception as e:
            print(e)
            break
