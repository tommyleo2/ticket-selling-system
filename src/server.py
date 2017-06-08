import tornado.ioloop
from application import application
from test import test_schema
from utility.config import g_config

import sys


def start():
    application.listen(g_config.get("App", "port", fallback=9999))
    tornado.ioloop.IOLoop.current().start()


def test():
    test_schema.test()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "start":
            start()
        elif sys.argv[1] == "test":
            test()
    else:
        print("unrecognized cmd, exiting...")
