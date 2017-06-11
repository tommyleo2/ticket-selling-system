# Ticket Selling System

A simple ticket selling system project using flask, sqlalchemy, mysql, deployed with docker

[![Build Status](https://travis-ci.org/tommyleo2/ticket-selling-system.svg?branch=master)](https://travis-ci.org/tommyleo2/ticket-selling-system)

Built and tested on 
- docker 17.05.0-ce, build 89658be
- docker-compose version 1.8.0, build f3628c7


## Design

- Database Design: [Design diagram](doc/database_design.md)
- API Documentation: [API](doc/API_doc.md) 

## Quick Start

### Deploy to host

#### Prerequisite

- python3.5
- mysql5.7
- [python modules](requirements.txt)
    - flask==0.12
    - sqlalchemy==1.1.10
    - flask_sqlalchemy==2.2
    - flask_hashing==1.1
    - configparser==3.5.0
    - pymysql==0.7.9
    - mixer==5.6.6
 
#### Step

1. Goto project root directory, execute `sudo pip3 install -r requirements.txt` to install python modules
2. Modify configuration file in `src/config.d/config.conf` with your special needs
3. Ensure mysql database is set as in `config.conf` file
4. Goto `src/` and execute `python3 server.py start` and you are all set
     
### Deploy to docker

#### Prerequisite

- docker
- docker-compose
   
#### Step

1. Goto `docker/`
2. Put `.env` file in it. The contents are documented later
3. Execute `docker-compose up -d` and you are all set

#### Note

Do not modify `src/config.d/config.conf` when you deploy to docker

#### `.env` File

- `TICKET_SERVER_CMD`
    - `start`
      Run server
    - `test`
      Run test and exit
- `TICKET_SERVER_PORT`
    - `9999`
      Deloying port

## Look into deeper

### Flask Session

Flask session is based on cookies, and you must set a secret key to it so that the cookies are encrypted and cannot be read by others
The secret key is set in `src/app/__init__.py` and is not configurable in `config.conf`file. It is recommanded to use a random string as secret key, just as documented in [Flask quick start](http://flask.pocoo.org/docs/0.12/quickstart/#sessions)

### Database fake data

Python module `mixer` is a fake data generator. To auto-generate data and store them into database, you can start the server with test parameter (pass `test` as parameter when run in host, or set `TICKET_SERVER_PORT=test`in .env file when run in docker)
Problem is that it cannot deal with FK in a good manner, so to create tickets, you must insert to database on your own.
More usage is documented in [here](https://mixer.readthedocs.io/en/latest/quickstart.html#sqlalchemy-orm)

### Password hashing

Passwords are hashed and not salted before they are stored into database. To have customed pasword hashing, reference [flask_hashing](http://flask-hashing.readthedocs.io/en/latest/)

## Things can be improved

1. Seperate routers and handlers
2. Some basic operation can be encapsulated into models
3. Log system
4. Distributed system, with nginx as proxy server
5. Database cluster and data backup
6. Cache movie and cinema infomation in Redis

...