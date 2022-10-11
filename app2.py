#Original test file from: https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

from flask import Flask, abort, render_template
from markupsafe import escape
import datetime
import calendar
import csv
from pathlib import Path
app = Flask(__name__)


@app.route('/')
def home():
    data = {
        'utc_dt':date_time_str,
        'day':today,
        'file':table
    }
    return render_template('index.html', data=data)

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
today = calendar.day_name[now.weekday()]

file = Path(r'C:\Users\sam\webdev\timecheck\template.csv')
table={}
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            table['headers'] = row
            line_count +=1
        else:
            table[str(line_count)]=row
            line_count +=1
            continue
