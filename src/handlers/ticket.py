import tornado


class TicketHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello Ticket")
