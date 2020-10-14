# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1', 8945))
import optparse
import socket
import json


class ClientHandle:
    def __init__(self):
        self.op = optparse.OptionParser()
        self.op.add_option("-s", "--server", dest="server")
        self.op.add_option("-p", "--port", dest="port")
        self.op.add_option("-u", "--username", dest="username")
        self.op.add_option("-P", "--password", dest="password")

        self.options, self.args = self.op.parse_args()

        self.verify_args(self.options, self.args)
        self.make_connection()

    def verify_args(self, options, args):
        server = options.server
        port = options.port
        username = options.username
        password = options.password

        if int(port) > 0 and int(port) < 65535:
            return True
        else:
            exit("the port is round 0-65535")

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server, int(self.options.port)))

    def interactive(self):
        if self.authenticate_one():
            pass
        data = {
            "action": "auth",
            "username":self.options.username,
            "password":self.options.password,
        }
        self.sock.send(json.dumps(data).encode('utf-8'))
        response = self.response()

    def authenticate_one(self):
        while True:
            if not (self.options.username and self.options.password):
                print('Wrong username&password!\nPlease input')
                self.options.username = input("username:")
                self.options.password = input("password:")
            return True

    def response(self):
        data = self.sock.recv(1024).decode('utf-8')
        data = json.loads(data)
        return data
    #
    # def get_auth_result(self, user, pwd):
    #     data = {
    #         "action":"auth",
    #         "username":user,
    #         "password":pwd,
    #     }
    #     self.sock.send(json.dumps(data).encode('utf-8'))
    #     response = self.response()



