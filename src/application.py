import tornado.web
from handlers.index import IndexHandler
from handlers.signin import SigninHandler
from handlers.signout import SignoutHandler
from handlers.signup import SignupHandler
from handlers.ticket import TicketHandler

application = tornado.web.Application([
    ("/", IndexHandler),
    ("/signin", SigninHandler),
    ("/signout", SignoutHandler),
    ("/signup", SignupHandler),
    ("/ticket", TicketHandler)
])
