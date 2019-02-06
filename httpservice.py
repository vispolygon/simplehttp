#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import os
import argparse

parser = argparse.ArgumentParser(description='Start Http Service')
parser.add_argument('--port', dest='port', type=int, default=8000,
                   help='Port Number (default: 8000)', metavar='port')

args = parser.parse_args()

'''
Change the current folder to public
'''
home_dir = os.path.join(os.path.dirname(__file__), 'public')
os.chdir(home_dir)

'''
Start http service
'''
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", args.port), Handler)

print "Serving at port", args.port
httpd.serve_forever()

