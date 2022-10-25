#Original test file from: https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

from flask import Flask, abort, render_template, request
from markupsafe import escape
import getpass
import os
import datetime
from datetime import timedelta
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
# set FLASK_DEBUG=True

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
        dateWorked = request.form.get("workedDate")
        hours = request.form.get("HourInput")
        comment = request.form.get("commentInput")
        timestamp =datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        payload = {"timestamp": timestamp,
                    "subject": subject,
                    "dateWorked": dateWorked,
                    "hours": hours,
                    "comment": comment,
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
            'month':month,
            'file':table,
            'engineer':engineer,
            'jobs':jobs,
            'dates':dates,
            'aggFile': aggFunct(file2)}
        thisWeek()
        return render_template("timekeeper.html", timekeeperdata=timekeeperdata)

now = datetime.datetime.now()
date_time_str = now.strftime("%m-%d-%Y %H:%M:%S")
today = calendar.day_name[now.weekday()]
month = calendar.month_name[now.weekday()]
dates = datetime.date#calendar.weekheader(10)



home_template = Path(r'C:\Users\sam\webdev\timecheck\template.csv')
laptop_template = Path(r'C:\Users\samsl\OneDrive\Desktop\timeCheck\template2.csv')
work_template = Path(r'X:\Sam Slusky\web\timeCheck\template.csv')

home_template2 = Path(r'C:\Users\sam\webdev\timecheck\template2.csv')
work_template2 = Path(r'X:\Sam Slusky\web\timeCheck\template2.csv')

home_controller = Path(r'C:\Users\sam\webdev\timecheck\controller.csv') # column name: Categorys,Projects,Engineers,Team
work_controller = Path(r'X:\Sam Slusky\web\timeCheck\controller.csv')
laptop_controller = Path(r'C:\Users\samsl\OneDrive\Desktop\timeCheck\controller.csv')

table={}
computers = ['home', 'laptop', 'work']
location = computers[1]


if location == 'work' :
    file = work_template
    file2 = work_template2
    controller = work_controller
elif location == 'home':
    file = home_template
    file2 = home_template2
    controller = home_controller
elif location =='laptop':
    file = file2 = laptop_template
    controller = laptop_controller

    
with open(file2) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            table['headers'] = row[1:]
            line_count +=1
        else:
            table[str(line_count)]=row[1:]
            line_count +=1
    
            

with open(controller) as csv_controller:
    df = pd.read_csv(csv_controller)
    user = os.getlogin()#getpass.getuser()
    #print("user", user)
    engineer = [user, df[df['Engineers']==user].Team.item()]
    #print(engineer)
    jobs = {"category":df['Categorys'].tolist(), "projects":df['Projects'].tolist()}

            

def update_csv(filename, data):
    print("updating CSV")
    field_names = list(data.keys())
    with open(filename, 'a', newline="") as file_object:
        dictwriter_object= DictWriter(file_object, fieldnames=field_names)
        dictwriter_object.writerow(data)
        file_object.close()
    print(data)

#I want to create a function that will aggregate the project/category time for a given engineer
def aggFunct(filename):
    df = pd.read_csv(filename)
    df_grouped = df.groupby(by="category")["hours"].sum().to_dict()
    print(df_grouped)
    return df_grouped

def thisWeek():
    Dict = {}
    for wn,d in enumerate(allsundays(datetime.datetime.now().year)):
        Dict[wn+1] = [(d + timedelta(days=k)).isoformat() for k in range(0,7)]
    print('This week is:')
    print(date_time_str)
    print(today)
    print(datetime.date.today())
    print(now.isocalendar())

    week = Dict[now.isocalendar()]
    print(week)

    
def allsundays(year): #https://stackoverflow.com/questions/2003841/how-can-i-get-the-current-week-using-python
    """This code was provided in the previous answer! It's not mine!"""
    d = datetime.date(year, 1, 1)                    # January 1st                                                          
    d += timedelta(days = 6 - d.weekday())  # First Sunday                                                         
    while d.year == year:
        yield d
        d += timedelta(days = 7)





if __name__=='__main__':
   app.run()
