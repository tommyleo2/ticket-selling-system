from app import app
from app import hashing
from app.models import (User, Cinema, Movie, ShowIn, TimeTable,
                        Ticket, TicketInOrder, Order)


from mixer.backend.flask import mixer
import datetime


def test():
    fake_data()


def fake_data():
    mixer.init_app(app)

    mixer.cycle(50).blend(User, password=hashing.hash_value("123456"))
    mixer.cycle(10).blend(Cinema, info=mixer.sequence("info_{0}"))
    mixer.cycle(10).blend(Movie, length=(a for a in range(95, 126)))
    # mixer.cycle(20).blend(ShowIn)
    # mixer.cycle(100).blend(TimeTable)
    # mixer.cycle(1000).blend(Ticket)
    # mixer.cycle(50).blend(Order)
    # mixer.cycle(50).blend(TicketInOrder)
