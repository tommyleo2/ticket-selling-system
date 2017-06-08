from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy import Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, index=True)
    email = Column(String(64), nullable=False)
    phone = Column(String(20))
    password = Column(CHAR(128), nullable=False)


class Order(Base):
    __tablename__ = "order"
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"),
                     nullable=False, index=True)
    order_at = Column(DateTime, default=datetime.datetime.now)
    user = relationship("User")
    ticket_in_order = relationship("TicketInOrder")


class TicketInOrder(Base):
    __tablename__ = "ticket_in_order"
    order_id = Column(Integer, ForeignKey("order.order_id"), primary_key=True)
    ticket_id = Column(Integer, ForeignKey("ticket.ticket_id"), nullable=False)
    order = relationship("Order")
    ticket = relationship("Ticket")


class Ticket(Base):
    __tablename__ = "ticket"
    ticket_id = Column(Integer, primary_key=True)
    cinema_id = Column(Integer, ForeignKey("cinema.cinema_id"),
                       nullable=False, index=True)
    movie_id = Column(Integer, ForeignKey("movie.movie_id"),
                      nullable=False, index=True)
    timetable_id = Column(Integer, ForeignKey("timetable.timetable_id"))
    room = Column(String(10), nullable=False)
    seat = Column(String(10), nullable=False)
    cinema = relationship("Cinema")
    movie = relationship("Movie")
    ticket_in_order = relationship("TicketInOrder")
    timetable = relationship("TimeTable")


class Cinema(Base):
    __tablename__ = "cinema"
    cinema_id = Column(Integer, primary_key=True)
    cinema_name = Column(String(64), nullable=False)
    info = Column(Text)


class Movie(Base):
    __tablename__ = "movie"
    movie_id = Column(Integer, primary_key=True)
    movie_name = Column(String(64), nullable=False, index=True)
    length = Column(Integer, nullable=False)
    info = Column(Text)
    show_in = relationship("ShowIn")


class ShowIn(Base):
    __tablename__ = "show_in"
    showin_id = Column(Integer, primary_key=True)
    cinema_id = Column(Integer, ForeignKey("cinema.cinema_id"),
                       nullable=False, index=True)
    movie_id = Column(Integer, ForeignKey("movie.movie_id"),
                      nullable=False, index=True)
    cinema = relationship("Cinema")
    movie = relationship("Movie")
    timetable = relationship("TimeTable")


class TimeTable(Base):
    __tablename__ = "timetable"
    timetable_id = Column(Integer, primary_key=True)
    showin_id = Column(Integer, ForeignKey("show_in.showin_id"),
                       index=True)
    start_at = Column(DateTime, nullable=False)
    show_in = relationship("ShowIn")
