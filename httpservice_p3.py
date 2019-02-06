import http.server
import socketserver
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

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
