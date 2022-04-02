from tornado import ioloop, web


class MainHandler(web.RequestHandler):
    def get(self):
        self.write('Hello, world')


def make_app():
    return web.Application([
        (r'/', MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()

'''
curl http://localhost:8888/

Hello, world
'''
