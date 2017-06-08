from flask_sqlalchemy import SQLAlchemy

from app import app
from app.utility.config import g_config

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{user}:{password}@{server}:3306/{database}?\
charset=utf8".format(user=g_config.get("MySQL", "username"),
                     password=g_config.get("MySQL", "password"),
                     server=g_config.get("MySQL", "server"),
                     database=g_config.get("MySQL", "database"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class BaseModel(object):
    def insert(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self


from .cinema import Cinema
from .movie import Movie
from .order import Order
from .show_in import ShowIn
from .ticket import Ticket
from .ticket_in_order import TicketInOrder
from .timetable import TimeTable
from .user import User
