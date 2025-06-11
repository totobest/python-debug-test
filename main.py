from google.appengine.api import wrap_wsgi_app
from wsgiref.simple_server import make_server

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield b'Hello world!\n'

app = wrap_wsgi_app(app)

with make_server('', 8000, app) as httpd:
    print("Listening on port 8000....")
    httpd.serve_forever()