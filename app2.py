#Original test file from: https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

from flask import Flask, abort, render_template, request
from markupsafe import escape
import getpass
import os
import datetime
import calendar
import csv
from csv import DictWriter
from pathlib import Path
import pandas as pd

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


#To start on development, need to enter the following information
# set FLASK_APP=app2
# set FLASK_ENV=developement

#On work computer running the app requires the command, "python -m flask run"
#On home computer running the app


@app.route('/', methods=["GET","POST"])
def home():
    data = {
        'utc_dt':date_time_str,
        'day':today,
        'file':table,
        'engineer':engineer,
        'jobs':jobs
    }
    if request.method == "POST":
        
        subject = request.form.get("CategoryInput")
        dayWorked = request.form.get("DayInput")
        hour = request.form.get("HourInput")
        comment = request.form.get("commentInput")
        timestamp =datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        payload = {"subject": subject,
                    "dayWorked": dayWorked,
                    "hour": hour,
                    "comment": comment,
                    "timestamp": timestamp,
                    }
        update_csv(file2, payload)
        
        #print("output: ", subject, dayWorked, hour, comment, timestamp)
    return render_template('index.html', data=data)

@app.route('/engineers/')
def engineers():
    engineers = ["Trevor",
                "Bill",
                "Nate",
                "Sam",
                "Ezekiel"]
    return render_template("engineers.html", engineers=engineers)

@app.route('/timekeeper/')
def timekeeper():
        timekeeperdata = {
            'utc_dt':date_time_str,
            'day':today,
            'file':table,
            'engineer':engineer,
            'jobs':jobs}
        return render_template("person.html", timekeeperdata=timekeeperdata)

now = datetime.datetime.now()
date_time_str = now.strftime("%m-%d-%Y %H:%M:%S")
today = calendar.day_name[now.weekday()]



home_template = Path(r'C:\Users\sam\webdev\timecheck\template.csv')
work_template = Path(r'X:\Sam Slusky\web\timeCheck\template.csv')
home_template2 = Path(r'C:\Users\sam\webdev\timecheck\template2.csv')
work_template2 = Path(r'X:\Sam Slusky\web\timeCheck\template2.csv')
home_controller = Path(r'C:\Users\sam\webdev\timecheck\controller.csv') # column name: Categorys,Projects,Engineers,Team
work_controller = Path(r'X:\Sam Slusky\web\timeCheck\controller.csv')
table={}
work = False


if work:
    file = work_template
    file2 = work_template2
    controller = work_controller
else:
    file = home_template
    file2 = home_template2
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
            

with open(controller) as csv_controller:
    df = pd.read_csv(csv_controller)
    user = os.getlogin()#getpass.getuser()
    engineer = [user, df[df['Engineers']==user].Team.item()]
    #print(engineer)
    jobs = {"category":df['Categorys'].tolist(), "projects":df['Projects'].tolist()}


with open(file2) as csv_file2:
    csv_reader2 = csv.reader(csv_file2, delimiter=',')
    line_count = 0
    for row in csv_reader2:
        if line_count == 0:
            table['headers'] = row
            line_count +=1
        else:
            table[str(line_count)]=row
            line_count +=1
            

def update_csv(filename, data):
    print("updating CSV")
    field_names = list(data.keys())
    with open(filename, 'w', newline="") as file_object:
        dictwriter_object= DictWriter(file_object, fieldnames=field_names)
        dictwriter_object.writerow(data)
        file_object.close()
    print(data)


if __name__=='__main__':
   app.run()
