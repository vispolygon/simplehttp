import SimpleHTTPServer
import SocketServer
import os

PORT = 8000
'''
Change the current folder to public
'''
home_dir = os.path.join(os.path.dirname(__file__), 'public')
os.chdir(home_dir)

'''
Start http service
'''
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving at port", PORT
httpd.serve_forever()

