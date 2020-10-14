# from socket import *
# ip_port = ('127.1.0.3', 8456)
# back_log = 5
# buffer_size = 1024
#
# tcp_server = socket(AF_INET, SOCK_STREAM)
# tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   # 服务器重启时重用ip地址
# tcp_server.bind(ip_port)
# tcp_server.listen(back_log)
#
# conn, addr = tcp_server.accept()