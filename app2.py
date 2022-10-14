#Original test file from: https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

from flask import Flask, abort, render_template
from markupsafe import escape
import getpass
import os
import datetime
import calendar
import csv
from pathlib import Path
import pandas as pd

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


#To start on development, need to enter the following information
# set FLASK_APP=app2
# set FLASK_ENV=developement

#On work computer running the app requires the command, "python -m flask run"
#On home computer running the app


@app.route('/')
def home():
    data = {
        'utc_dt':date_time_str,
        'day':today,
        'file':table,
        'engineer':engineer,
        'jobs':jobs
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

work = True

home_template = Path(r'C:\Users\sam\webdev\timecheck\template.csv')
work_template = Path(r'X:\Sam Slusky\web\timeCheck\template.csv')
home_controller = Path(r'C:\Users\sam\webdev\timecheck\controller.csv') # column name: Categorys,Projects,Engineers,Team
work_controller = Path(r'X:\Sam Slusky\web\timeCheck\controller.csv')
table={}

if work:
    file = work_template
    controller = work_controller
else:
    file = home_template
    controller = home_controller
    
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

with open(controller) as csv_controller:
    df = pd.read_csv(csv_controller)
    user = os.getlogin()#getpass.getuser()
    engineer = [user, df[df['Engineers']==user].Team.item()]
    #print(engineer)
    jobs = {"category":df['Categorys'].tolist(), "projects":df['Projects'].tolist()}
    #print (jobs['category'])
