#Original test file from: https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

from flask import Flask, abort, render_template
from markupsafe import escape
import datetime
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=date_time_str)

@app.route('/engineers/')
def engineers():
    engineers = ["Trevor",
                "Bill",
                "Nate",
                "Sam",
                "Ezekiel"]
    return render_template("engineers.html", engineers=engineers)

@app.route('/person/')
def person():
    persons = ["Trevor",
                "Bill",
                "Nate",
                "Sam",
                "Ezekiel"]
    return render_template("person.html", persons=persons)

now = datetime.datetime.now()
date_time_str = now.strftime("%m-%d-%Y %H:%M:%S")