from flask import Flask
from flask_hashing import Hashing

app = Flask(__name__)
app.config["SECRET_KEY"] = b"\x9f\x89~i\x8b\xa5s\x1b=\xe4\xb49\xc2\x06\x81\x0e\xeeE;'\xdc\x87\xf66"
hashing = Hashing(app)

from .handlers import *
