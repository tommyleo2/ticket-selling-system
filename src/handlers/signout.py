import tornado


class SignoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Signout")
