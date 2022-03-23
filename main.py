from crypt import methods
from flask import Blueprint, Flask, redirect, render_template, send_from_directory, request, url_for
from __init__ import create_app, db

from flask import jsonify

import user

main = Blueprint('main', __name__)

app = create_app()
db.create_all(app=app)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", **{'value': user.getQtt(request.remote_addr)})

@main.route('/send', methods=['POST'])
def recieve():
    if not user.recieveData(request.remote_addr, request.get_json(force=True)):
        return redirect("/", code=400)
    return ''


@main.route('/vancauwenberghe', methods=['GET',"POST"])
def vancauwenberghe():
    return render_template("admin.html")


@main.route('/vancauwenberghe_send', methods=['POST'])
def vancauwenberghe_send():
    user.validateAllUsers(int(request.get_json()["val"]))
    return render_template("admin.html")


@main.route('/js/<name>.js')
def sendScript(name):
    return send_from_directory("./scripts", name + ".js")


@main.route('/styles/<name>.css')
def sendStyle(name):
    return send_from_directory("./resources", name + ".css")

@main.route('/resources/<name>')
def sendResource(name):
    return send_from_directory("./resources/", name)


if __name__ == '__main__':
    db.create_all(app=app)
    app.run(host='0.0.0.0', debug=True)