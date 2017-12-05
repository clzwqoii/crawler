import tornado.web
import tornado.ioloop
import apiServer

application = tornado.web.Application([
    (r"/", apiServer.Reptilian),
])
if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()