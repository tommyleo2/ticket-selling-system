from models.models import *
from sqlalchemy import create_engine
from utility.config import g_config


def test():
    mysql_uri = "mysql+pymysql://{user}:{password}@{server}:3306/{database}?\
charset=utf8".format(user=g_config.get("MySQL", "username"),
                     password=g_config.get("MySQL", "password"),
                     server=g_config.get("MySQL", "server"),
                     database=g_config.get("MySQL", "database"))

    engine = create_engine(mysql_uri)
    Base.metadata.create_all(engine)
