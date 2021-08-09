#!/usr/bin/python
# -*- coding: UTF-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import json
import socket

data = {'result': 'this is a test'}
host = ('localhost', 8888)
ip = ''


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        global ip
        print(self.client_address, self.path)
        if self.path.startswith('/do'):
            ip = self.client_address[0]
            event.set()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


class SocketThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.con = socket.socket()

    def run(self):
        print(socket.gethostname())
        self.con.connect(('127.0.0.1', 12345))
        self.listen()
        # event.wait()
        # self.send()

    def listen(self):
        while True:
            rec = self.con.recv(1024)
            print(rec.decode())
            if rec.decode() == 'ok':
                print('消息正常结束')
            if not rec:
                print('链接断开了')
            break
        event.clear()
        event.wait()
        self.send()

    def send(self):
        print('尝试发送消息')
        self.con.send(('do_' + ip).encode())
        self.listen()


if __name__ == '__main__':
    event = threading.Event()
    client = SocketThread()
    client.start()
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
