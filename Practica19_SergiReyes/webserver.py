# -*- coding: utf-8 -*-
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# http://pymotw.com/2/BaseHTTPServer/
class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if "practica.html" in self.path:
            file = open("practica.html", 'rb')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(file.read())
        else:
            self.send_error(404, "Not Found")


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
