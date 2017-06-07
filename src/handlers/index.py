import tornado
import tornado.template


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_secure_cookie("user"):
            pass
        else:
            self.redirect("/signin")
