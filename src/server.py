#!/usr/bin/env python3

from app import app
from test import test_schema
import sys


def start():
    app.run()


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
