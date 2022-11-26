scratch



#Script that is reading the controller CSV to fill lists and engineer data
with open(controller) as csv_controller:
    df = pd.read_csv(csv_controller)
    user = os.getlogin()
    #print("user", user)
    engineer = [user, df[df['Engineers']==user].Team.item()]
    #print(engineer)
    jobs = {"category":df['Categorys'].tolist(), "projects":df['Projects'].tolist()}
    print("JOBS", jobs)

    #This is creating a dictionary with the category and date and then the sum of hours worked on that date
    df_grouped = this_week.groupby(by=["category", "dateworked"])["hours"].sum().to_dict()
    print("df_grouped", df_grouped)
    #df_grouped2 and 3 aren't both necessary, just working on how I want to get the data organized. Probably will drop group 2.
    #thinking I want something like { date: [Category, hours]} as my datastructure, but not sure how well that will work in pandas
    # Want to play around with that structure.
    df_grouped2 = []
    df_grouped3 = {}
    for key, value in df_grouped.items():
        df_grouped2.append([key[0], key[1], value])
    print(df_grouped2)
    for key, value in df_grouped.items():
        df_grouped2.append([key[0], key[1], value])
    for key, value in df_grouped.items():
        if key[1] in df_grouped3.keys():
            df_grouped3[key[1]].append([key[0], value])
        else:
            df_grouped3[key[1]]=[[key[0], value]]"
    
    #this_week = pd.DataFrame.from_dict(categories, orient="index", columns=week)
    return df_grouped2

def aggFunct(filename, time):
    df = pd.read_csv(filename)
    if len(time) > 1:
        #print("time", time)
        this_time = df.loc[df['dateworked'].isin(time)] #selecting records for the given week
        print(this_time)
        df_grouped = this_time.groupby(by="category")["hours"].sum().to_dict()
    else:
        df_grouped = df.groupby(by="category")["hours"].sum().to_dict()
        #print("all", df_grouped)
    print("df_grouped", df_grouped)
    return df_grouped


    if request.method == "POST":
        time_period = request.form.get("aggregate")
        print("time_period", time_period)
        if time_period == "week":
            time = getWeek()
            print("WEEK: ", aggFunct(file2, time))
            return aggFunct(file2, time)
        elif time_period == "month":
            thismonth = getMonth()
            print("MONTH: ", aggFunct(file2, thismonth))
            return aggFunct(file2, thismonth)
        else:
            year = getYear()
            print("YEAR: ", aggFunct(file2, year))
            return aggFunct(file2, year)

<!--<table id="myTable">
      <tr>
        <th>Category</th>
        <th>Total Hours</th>
      </tr>
      {% for key, value in timekeeperdata['totalByCategory'].items() %}
        <tr>
          <td>{{key}}</td>
          <td>{{value}}</td>
        </tr>
      {% endfor %}
      </table> -->



      
  radioButton.forEach( radio => {
  radio.addEventListener("change", (event) => {
    console.log("radio button changed")
    if (radio[0] == "checked"){
      console.log("radio week")
      weekCategory.style.display = "flex"
      monthCategory.style.display = "none"
      yearCategory.style.display = "none"
    }
    else if (radio[1] == "checked"){
      console.log("radio month")
      weekCategory.style.display = "none"
      monthCategory.style.display = "flex"
      yearCategory.style.display = "none"
    }
    else if (radio[2] == "checked"){
      console.log("radio year")
      weekCategory.style.display = "none"
      monthCategory.style.display = "flex"
      yearCategory.style.display = "none"
    }
    })})