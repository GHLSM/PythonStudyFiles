from socket import *

ip_port = ('127.1.0.3', 8456)
back_log = 5
buffer_size = 1024
place = 'gbk'

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    cmd = input('>>:').strip()
    if not cmd:
        continue
    if cmd=='quit':
        break
    udp_client.sendto(cmd.encode('utf-8'), ip_port)
    cmd_res, addr = udp_client.recvfrom(buffer_size)
    print('处理结果为', cmd_res.decode(place))

udp_client.close()