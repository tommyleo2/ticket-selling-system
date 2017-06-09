from flask import request, session, make_response
import json

from app import app
from app import hashing
from ..models import User


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':

        if 'id' in session:
            # print("already signed in")
            return '', 200

        name = request.form.get("name", None)
        password = request.form.get("password", None)

        errorMsg = None

        if name is None:
            errorMsg = "name"
        elif password is None:
            errorMsg = "password"

        if errorMsg is not None:
            return json.dumps({
                "message": errorMsg + " is not provided"
            }), 400

        password = hashing.hash_value(password)
        user = User.query.filter_by(name=name).first()

        if user is None:
            return json.dumps({
                "message": "user not registered"
            }), 404
        if user.password != password:
            return json.dumps({
                "message": "password incorrect"
            }), 404

        session["id"] = user.user_id
        resp = make_response()
        return resp

    else:
        return json.dumps({"msg": "GET"})
