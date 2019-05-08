with open("state_crime-CS152.csv", "r") as file:
    print("State" + " "*12, "Reported Crimes")
    next(file)
    for aline in file:
        values = aline.split(',')
        state = values[10]
        totalp = int(values[11])
        totalv = int(values[15])
        sum = (totalp + totalv)
        mydict = dict([(state,sum)])
        for (k,v) in mydict.items():
            print("{:<21} {:>10,d}".format(k, v))
