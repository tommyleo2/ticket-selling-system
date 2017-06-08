from flask import request, session

from app import app


@app.route("/signout", methods=['GET', 'POST'])
def signout():
    if request.method == 'POST':
        session.pop('name', None)
        return '', 200
