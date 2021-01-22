#!/usr/bin/env python3
"""
The Priest WebServer https://github.com/sinsinsecurity/Priest
Usage::
    ./server.py [<port>]
"""
import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging
import sys

if(len(sys.argv) < 2):
    print("[!] No port specified, using default port :8000")
    PORT=8000
else:
    PORT = int(sys.argv[1])



print("[*] the Priest is listening on address http://0.0.0.0:%d" % PORT)

class GetHandler(
        SimpleHTTPServer.SimpleHTTPRequestHandler
        ):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()


