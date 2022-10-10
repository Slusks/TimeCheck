#Original test file from: https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3

from flask import Flask, abort
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    return "<h1>It's working!!</h1>"

@app.route('/tracker/')
def tracker():
    return "<h3> This is where the tracker will go </h3>"

@app.route('/capitalize/<word>/')
def capitalize(word):
    return "<h1>{}<h1>".format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>')
def add(n1, n2):
    return "<h1>{}</h1>".format(n1**n2)

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)