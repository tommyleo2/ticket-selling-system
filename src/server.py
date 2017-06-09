#!/usr/bin/env python3

from app import app
from test import test_all
from app.utility.config import g_config

import sys


def start():
    app.run(host="0.0.0.0", port=g_config["App"].get("port", 9999))


def test():
    test_all()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "start":
            start()
        elif sys.argv[1] == "test":
            test()
    else:
        print("unrecognized cmd, exiting...")
