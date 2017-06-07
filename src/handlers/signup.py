import tornado


class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Signup")
