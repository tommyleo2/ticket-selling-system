import configparser

g_config = configparser.ConfigParser()
g_config.read("config.d/config.conf")

#  MySQL configuration check
try:
    g_config["MySQL"]["server"]
    g_config["MySQL"]["username"]
    g_config["MySQL"]["password"]
    g_config["MySQL"]["database"]
except KeyError as e:
    raise KeyError("Cannot find key: MySQL.%s" % e.args)
