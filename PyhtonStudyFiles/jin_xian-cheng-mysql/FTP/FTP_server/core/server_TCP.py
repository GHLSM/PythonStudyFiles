import socketserver
import json


class ServerHandle(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        while True:
            data = self.request.recv(1024)
            data = data.decode('utf-8')
            data = json.loads(data)
            if data.get("action"):
                if hasattr(self, data.get('action')):
                    func = getattr(self, data.get('action'))
                    func(**data)
                else:
                    print("inValid cmd")
            else:
                print('Invalid cmd')

    def auth(self, **data):
        print(data)

    def put(self, **data):
        pass

