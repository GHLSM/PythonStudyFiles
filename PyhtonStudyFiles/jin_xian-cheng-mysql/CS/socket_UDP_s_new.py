from socket import *
import subprocess

ip_port = ('127.1.0.3', 8456)
buffer_size = 1024
place = 'gbk'

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    cmd, addr = udp_server.recvfrom(buffer_size)
    res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stderr= subprocess.PIPE,
                                   stdout= subprocess.PIPE,
                                   stdin= subprocess.PIPE)

    err = res.stderr.read()
    if err:
        com_res = err
    else:
        com_res = res.stdout.read()
    if not com_res:
            com_res = '执行成功，但无返回值'
            com_res.encode(place)

    udp_server.sendto(com_res, addr)





# print('新的客户链接为', addr)
# while True:
#     try:
#         cmd = conn.recv(buffer_size)
#         if not cmd:
#             break
#
#         print('收到用户的命令为', cmd)
#
#         res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
#                                stderr= subprocess.PIPE,
#                                stdout= subprocess.PIPE,
#                                stdin= subprocess.PIPE)
#
#         err = res.stderr.read()
#         if err:
#             com_res = err
#         else:
#             com_res = res.stdout.read()
#         if not com_res:
#             com_res = '执行成功，但无返回值'
#             com_res.encode(place)
#         conn.send(com_res)
#     except Exception as e:
#         print(e)
#         break

