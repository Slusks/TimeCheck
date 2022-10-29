scratch

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