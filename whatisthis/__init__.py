from http.server import HTTPServer
from controller import RequestHandler

def create_server(emitter, images, categories, port=8081):

    server_address = ('127.0.0.1', port)

    def Handler(*args):
        RequestHandler(test_emitter, images, categories, *args)

    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()
    return
