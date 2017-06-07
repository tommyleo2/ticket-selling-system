from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy import Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

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
    ticket_id = Column(Integer, ForeignKey("ticket.ticket_id"), nullable=False)
    user = relationship("User")
    ticket = relationship("Ticket")


class Cinema(Base):
    __tablename__ = "cinema"
    cinema_id = Column(Integer, primary_key=True)
    cinema_name = Column(String(64), nullable=False)
    info = Column(Text)


class Ticket(Base):
    __tablename__ = "ticket"
    ticket_id = Column(Integer, primary_key=True)
    cinema_id = Column(Integer, ForeignKey("cinema.cinema_id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movie.movie_id"), nullable=False)
    room = Column(String(10), nullable=False)
    seat = Column(String(10), nullable=False)
    start_at = Column(DateTime)
    cinema = relationship("Cinema")
    movie = relationship("Movie")


class Movie(Base):
    __tablename__ = "movie"
    movie_id = Column(Integer, primary_key=True)
    movie_name = Column(String(64), nullable=False, index=True)
    length = Column(Integer, nullable=False)
    info = Column(Text)


class ShowIn(Base):
    __tablename__ = "showin"
    cinema_id = Column(Integer, ForeignKey("cinema.cinema_id"),
                       nullable=False, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movie.movie_id"),
                      nullable=False, primary_key=True)
    cinema = relationship("Cinema")
    movie = relationship("Movie")
