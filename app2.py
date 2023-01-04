#Original test file from: https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

from flask import Flask, abort, render_template, request, url_for, jsonify
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
import json
import PYcontroller #This is going to be the controller file. Yay for refactoring!

pd.set_option('display.max_columns', 20)


app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

computers = ['home', 'laptop', 'work']
location = computers[2]



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
        'jobs':jobs,
        'rigData': rigData,
        'projectData': ProjectData,
        'allData': allData
    }
    if request.method == "POST":
        ##Shop only items .get(name)
        team = request.form.get("team")
        subject = request.form.get("CategoryInput")
        if len(request.form.get("workedDate")) <=0:
            dateWorked = date_time_str_rev
            print("date worked", dateWorked)
        else:
            dateWorked = request.form.get("workedDate")
        hours = request.form.get("HourInput")
        comment = request.form.get("commentInput")
        timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        if team == "shop":
            print("team:",  team)
            payload = {"timestamp": timestamp,
                        "category": subject,
                        "shop": "NA-SHOP",
                        "status": "NA-SHOP",
                        "type": "NA-SHOP",
                        "rig": "NA-SHOP",
                        "project": "NA-SHOP",
                        "desc": "NA-SHOP",
                        "dateWorked": dateWorked,
                        "hours": hours,
                        "comment": comment,
                        "engineer":engineer[0],
                        "team": team
                        }    
        elif team == "rig":
            category = request.form.get("subject")
            print("team: ", team)
            print("category: ", category)
            if category == "Project":
                shop = "NA"
                status = request.form.get("topic")
                type = "NA"
                rig = "NA"
                project = request.form.get("chapter")
                desc = "NA"
            elif category == "Admin":
                shop = "NA"
                status = "NA"
                type = request.form.get("topic")
                rig = "NA"
                project = "NA" 
                desc = request.form.get("chapter")
            elif category == "Troubleshooting":
                print("category is Troubleshooting")
                shop = request.form.get("topic")
                status = "NA"
                type = "NA"
                rig = request.form.get("chapter")
                project = "NA" 
                desc = "NA"                  
            payload = {"timestamp": timestamp,
                        "category": category,
                        "shop": shop,
                        "status": status,
                        "type": type,
                        "rig": rig,
                        "project": project,
                        "desc": desc,
                        "dateWorked": dateWorked,
                        "hours": hours,
                        "comment": comment,
                        "engineer":engineer[0],
                        "team": team
                        }            
        update_csv(file2, payload)
        
    return render_template('index.html', data=data)

@app.route('/administration/', methods=["GET","POST"] )
def administration():
    data= {
        "engineers": dict(control_engineers[location]),
        "rigTeam": control_rig,
        "shopTeam": control_shop,
        'role': PYcontroller.engineers[location][user][1],
        'rigData': rigData,
        'allData': allData
    }
    #.get(name)
    if request.method == "POST":
        if "changeEngineer" in request.form:
            engineer_name = request.form.get('EngineerInput')
            if engineer_name == "New":
                newEngineerID = request.form.get('engineerIDInput')
                newTeam = request.form.get('teamInput')
                newRole = request.form.get('roleInput')
                newStatus = "active"
                newEngineerName = request.form.get('engineerName')
                payload = {
                    newEngineerID:[
                        newTeam,
                        newRole,
                        newStatus,
                        newEngineerName
                    ]}
                print("new", payload)
            else:
                oldEngineerID = request.form.get('oldengineerIDInput')
                oldTeam = request.form.get('oldteamInput')
                oldRole = request.form.get('oldroleInput')
                oldStatus = request.form.get('oldroleInput')
                oldEngineerName = request.form.get('oldengineerName')
                payload = {
                    oldEngineerID:[
                        oldTeam,
                        oldRole,
                        oldStatus,
                        oldEngineerName
                    ]}
                print ("old:", payload)  

            print("changeEngineer")

            
        elif "shopCategories" in request.form:
            print("shopCategories")
            
        elif "rigUpdates" in request.form:
            print("rigUpdates")
            
        elif "rigProjects" in request.form:
            print("rigProjects")
            
        else:
            print(request.form)
        
        print(payload)




    return render_template("administration.html", data=data)

@app.route('/timekeeper/', methods=["GET","POST"])
def timekeeper():
    timekeeperdata = {
        'utc_dt':date_time_str,
        'day':today,
        'month':month,
        'file':table,
        'engineer':engineer,
        'jobs':jobs,
        'dates':dates
        }
    weekTable = thisWeek(file2)
    weekCategory = aggDF(file2, getWeek())
    monthCategory = aggDF(file2, getMonth())
    yearCategory = aggDF(file2, getYear())


    return render_template("timekeeper.html", timekeeperdata=timekeeperdata, 
    tables=[full_hours.to_html(classes='data'),
        weekTable.to_html(classes='data'),
        weekCategory.to_html(classes='data'),
        monthCategory.to_html(classes='data'),
        yearCategory.to_html(classes='data')],
     titles=[full_hours.columns.values,
         weekTable.columns.values,
         weekCategory.columns.values,
         monthCategory.columns.values,
         yearCategory.columns.values])

#easy to use date/time variables
now = datetime.datetime.now()
date_time_str = now.strftime("%m-%d-%Y %H:%M:%S") # returns todays date
date_time_str_rev = now.strftime("%Y-%m-%d")
#print("date_time_str", date_time_str)
#print("date_time_str", date_time_str[0:10])
today = calendar.day_name[now.weekday()] # returns today
month = calendar.month_name[now.weekday()]
dates = datetime.date
days = ['Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


#These functions combine to get me a dict of every day in the year grouped by week with the 
#week number as the dict key
def getWeekDict():
    Dict = {}
    for wn,d in enumerate(allsundays(datetime.datetime.now().year)):
        Dict[wn+1] = [(d + timedelta(days=k)).isoformat() for k in range(0,7)]
    return Dict

def allsundays(year): #https://stackoverflow.com/questions/2003841/how-can-i-get-the-current-week-using-python
    """This code was provided in the previous answer! It's not mine!"""
    d = datetime.date(year, 1, 1)                    # January 1st                                                          
    d += timedelta(days = 6 - d.weekday())  # First Sunday                                                         
    while d.year == year:
        yield d
        d += timedelta(days = 7)


table={}



#This set of scripts is setting my file paths based on location. This is going to have to be
#greatly expanded as I build out file system.
"ctrl + / to comment a block"
if location == "home":
    try:
        file = Path(r'C:\Users\sam\webdev\timecheck\template.csv')
        file2 = Path(r'C:\Users\sam\webdev\timecheck\template2.csv')
        controller = Path(r'C:\Users\sam\webdev\timecheck\controller.csv') # column name: Categorys,Projects,Engineers,Team
    except:
        print("not home")
        pass
elif location =="laptop":
    try:
        file = file2 = Path(r'C:\Users\samsl\OneDrive\Desktop\timeCheck\template2.csv')
        controller = Path(r'C:\Users\samsl\OneDrive\Desktop\timeCheck\controller.csv')
        file3 = Path(r'C:\Users\samsl\OneDrive\Desktop\timeCheck\rigTemplate.csv')

    except:
        print("not on laptop")
        pass
else:
    print("at work")
    file = Path(r'X:\Sam Slusky\web\timeCheck\template.csv')
    file2 = Path(r'X:\Sam Slusky\web\timeCheck\template2.csv')
    controller = Path(r'X:\Sam Slusky\web\timeCheck\controller.csv')

full_hours = pd.read_csv(file2)


            
####################################################################################################
##REPLACING THE ABOVE SCRIPT FOR ACCESSING THE CONTROLLER FILE
user = os.getlogin()
engineer = [user, PYcontroller.engineers[location][user]]
#engineers = [key for d in PYcontroller.engineers for key in d.keys()]
print("engineer", engineer)
categoryShop = PYcontroller.category
#print("categoryShop", categoryShop)
categoryRig=[]
for i in PYcontroller.task:
    if type(i) == str:
        categoryRig.append(i)
    elif type(i) == dict:
        categoryRig.append(list(i.keys())[0])
#print("categoryRig", categoryRig)
jobs = {"category":categoryShop, "projects":categoryRig}

admin = PYcontroller.task[0]["Admin"]
rigData = PYcontroller.task[1]["Troubleshooting"]
ProjectData = PYcontroller.task[2]["project"]
allData = {"Admin": admin , "Troubleshooting": rigData, "Project":ProjectData}
#################################

#######################################
#New set of functions for controlling data in controller file

control_shop = PYcontroller.category
#print("contol_shop: ", control_shop)
control_rig = PYcontroller.task
#print("control_rig: ", control_rig)
control_engineers = PYcontroller.engineers
#print("control_engineers: ",control_engineers)

            
#Function that drops submitted data to a csv.
def update_csv(filename, data):
    #print("updating CSV")
    field_names = list(data.keys())
    with open(filename, 'a', newline="") as file_object:
        dictwriter_object= DictWriter(file_object, fieldnames=field_names)
        dictwriter_object.writerow(data)
        file_object.close()
    #print(data)

#I want to create a function that will aggregate the project/category time for a given engineer
#returns dataframe
def aggDF(filename, time): 
    df = pd.read_csv(filename)
    if len(time) > 1:
        #print("time", time)
        this_time = df.loc[df['dateworked'].isin(time)] #selecting records for the given week
        #print("this_time:", this_time)
        df_grouped = this_time.groupby(by="category")["hours"].sum().to_frame()
    else:
        df_grouped = df.groupby(by="category")["hours"].sum().to_frame()
        #print("all", df_grouped)
    #print("df_grouped", df_grouped)
    return df_grouped

#Function that returns a dataframe with the categories worked on this week
def thisWeek(filename):
    weekDict = getWeekDict()
    if now.isocalendar()[2] == 7: #this function doesn't work on Sunday if I dont put this if statement in. Not sure why
        weekNum = now.isocalendar()[1]+1
    else:
        weekNum = now.isocalendar()[1]
    print("WeekNum:", weekNum)
    week = weekDict[weekNum]
    df = pd.read_csv(filename)
    this_week = df.loc[df["dateworked"].isin(week)]
    this_week_formatted = this_week.groupby(['category','dateworked']).hours.sum().unstack().fillna("")
    for i in week:
        if i not in this_week_formatted.columns:
            this_week_formatted[i]= ""
    this_week_formatted = this_week_formatted.reindex(columns=week)
    column_dict = {}
    for i in days:
        ind = days.index(i)
        column_dict.update({week[ind]:i+'\n'+week[ind][5:]})
    #print(column_dict)
    this_week_formatted.rename(columns=column_dict, inplace=True)
    return this_week_formatted 

#function that returns a list of date strings for the current week YYYY-MM-DD
def getWeek() -> list: ##this should return a list of the days in the week in the format YYYY-MM-DD
    Dict = getWeekDict()
    if now.isocalendar()[2] == 7: #this function doesn't work on Sunday if I dont put this if statement in. Not sure why
        weekNum = now.isocalendar()[1]+1
    else:
        weekNum = now.isocalendar()[1]
    week= Dict[weekNum]
    return week

#Function that returns a list of date strings for the current month YYYY-MM-DD
def getMonth() -> list:
    Dict = getWeekDict()
    if now.isocalendar()[2] == 7: #this function doesn't work on Sunday if I dont put this if statement in. Not sure why
        weekNum = now.isocalendar()[1]+1
    else:
        weekNum = now.isocalendar()[1]
    cal = calendar.Calendar()
    #this should be the slice of the first item in the week dict value that represents the month
    month_val = int(Dict[weekNum][0][5:7])
    year = int(Dict[weekNum][0][:4])
    month_days = [ str(year) + "-" + str(month_val) + "-" + str(i).zfill(2) for i in cal.itermonthdays(year, month_val) if i > 0] 
    print("month_days:", month_days)
    return month_days

#Function that returns a list of date strings for the current year YYYY-MM-DD
def getYear() -> list:
    Dict = getWeekDict()
    yeardays = []
    for i in Dict.values():
        for j in i:
            yeardays.append(j)
    return yeardays








if __name__=='__main__':
   app.run()
