# -*- coding: utf-8 -*-
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import smtplib, ssl
# http://pymotw.com/2/BaseHTTPServer
password = "passwd"
context = ssl.create_default_context()

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if "practica.html" in self.path:
            file = open("practica.html", 'rb')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(file.read())
        elif "Liar_Club.png" in self.path:
            file = open("Liar_Club.png", 'rb')
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            self.wfile.write(file.read())
            #CORREU
            mail = smtplib.SMTP_SSL("smtp.gmail.com", 465) #connexió ssl
            mail.ehlo() #missatge de salutació amb el servei/servidor
            mail.login("sergireyes27@gmail.com", password) #login to gmail smtp
            message = "Subject: Hello There!" + "\n\n\nHa intentat entrar: %s" % str(self.client_address) #Cos del missatge
            mail.sendmail("sergireyes27@gmail.com", "sergireyes27@gmail.com", message) #envia el missatge
            mail.quit() 
        else:
            self.send_error(404, "Not Found")


if __name__ == '__main__':
    server = HTTPServer(('192.168.2.126', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'

    server.serve_forever()
