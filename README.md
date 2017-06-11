# Ticket Selling System

A simple ticket selling system project using flask, sqlalchemy, mysql, deployed with docker

[![Build Status](https://travis-ci.org/tommyleo2/ticket-selling-system.svg?branch=master)](https://travis-ci.org/tommyleo2/ticket-selling-system)

Build and tested on 
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
2. Put `.env` file in it. The content is documented later
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