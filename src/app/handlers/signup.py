from flask import request, session, make_response
import sqlalchemy
import json

from app import app
from app import hashing
from ..models import User


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if 'id' in session:
            # print("already signed up")
            session.pop('name', None)

        name = request.form.get("name", None)
        email = request.form.get("email", None)
        phone = request.form.get("phone", None)
        password = request.form.get("password", None)

        errorMsg = None

        if name is None:
            errorMsg = "name"
        elif email is None:
            errorMsg = "email"
        elif password is None:
            errorMsg = "password"

        if errorMsg is not None:
            return json.dumps({
                "message": errorMsg + " is not provided"
            }), 400

        password = hashing.hash_value(password)
        user = User(name=name, email=email, phone=phone, password=password)
        try:
            user.insert()
        except sqlalchemy.exc.IntegrityError as e:
            return json.dumps({
                "message": "user name registered"
            }), 409

        session["id"] = user.user_id
        resp = make_response()
        return resp

    else:
        return json.dumps({"msg": "GET"})
