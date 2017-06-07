import tornado


class SigninHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_secure_cookie("user"):
            self.redirect("/")

    def post(self):
        username = self.get_argument("user")
        password = self.get_argument("password")
        print(username, password)
