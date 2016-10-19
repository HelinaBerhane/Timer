# This Python file uses the following encoding: utf-8

### Import Modules ###
import sqlite3 # databases
import math
import time
import datetime

#--------------------#
#-- Initialisation --#
#--------------------#

# create the connection object that represents the database
connection = sqlite3.connect('time.db')
# create a Cursor object and call its execute() method to perform SQL commands:
c = connection.cursor()
# Create the tables
c.execute("CREATE TABLE IF NOT EXISTS time(type STRING(50), task STRING(100), time FLOAT)")

#---------------------#
#----- Functions -----#
#---------------------#

def mean(entry):
    # calculates the mean
    for row in c.execute("SELECT AVG(time) FROM time WHERE task = '"+ entry +"'"):
        return float(row[0])

def stanDev(entry):
    #calculates the standard deviation
    #sd = sqrt (sum(|x-x\bar|^2)/n)
    sm = 0.0
    mn = mean(entry)
    for row in c.execute("SELECT COUNT(*) FROM time WHERE task ='"+ entry +"'"):
        count = row
    for row in c.execute("SELECT * FROM time WHERE task = '"+ entry +"'"):
        sm = sm + (float(row[2]) - mn)**2
    return math.sqrt(sm/int(count[0]))

def predict(entry):
    prediction = "for "+ str(entry) + ": mean = " + str(mean(entry)) + "; standard deviation = " + str(stanDev(entry)) + "; prediction = " + str(mean(entry) + stanDev(entry))
    return prediction

def toUnix(x):
    unixTime = time.mktime(datetime.strptime(x, "%H:%M:%S").timetuple()
    return unixTime

def toTime(y):
    formattedTime = datetime.fromtimestamp(y).strftime('%H:%M:%S')
    return formattedTime

while True: 
    
    # ask for intention
    initialQuestion = input("Do you want to log a time (1), view your current logs (2), view predictions (3) or view the time (4)? - ")
    if initialQuestion == "1":
        
        # offer type reminder
        prompt1 = input("do you want to view the different types? y/n - ")
        if prompt1 == "y":
            for row in c.execute("SELECT DISTINCT type FROM time"):
                print(row)
        
        # ask for type
        typeQuestion = input("What type of task was it? e.g. Travel/Prep/Housework - ")
        
        # offer task reminder
        prompt2 = input("do you want to view the different tasks? y/n - ")
        if prompt2 == "y":
            for row in c.execute("SELECT DISTINCT task FROM time WHERE type = '" + typeQuestion + "'" ):
                 print(row)
        # ask for task
        taskQuestion = input("What task do you want to log? e.g. Travelling to uni - ")
        
        # ask for time
        timeQuestion = input("How long did it take you? [hh]:mm:ss - ")
        
        # confirm the entries
        print("Type: " + typeQuestion + "\nTask: " + taskQuestion + "\nQuestion: " + timeQuestion)
        
#        # ask for confirmation
        
        # add the inputs to the database
        logArr = [typeQuestion, taskQuestion, timeQuestion]
        c.execute("INSERT INTO time VALUES (?,?,?)", logArr)

        # commit changes
        connection.commit()
        
    elif initialQuestion == "2":
        
        # ask for intention
        prompt1 = input("do you want to see the logs for a specific type or task? - ")
        
        if prompt1 == "type":
            
            # offer reminder
            prompt2 = input("do you want to view the different types? y/n - ")
            if prompt2 == "y":
                for row in c.execute("SELECT DISTINCT type FROM time"):
                    print(row)
            
            # ask for intention
            prompt3 = input("what type do you want to see? - ")
            
            # print the table
            for row in c.execute("SELECT * FROM time WHERE type = '" + prompt3 + "'" ):
                 print(row)
            
        elif prompt1 == "task":
            
            # offer reminder
            prompt2 = input("do you want to view the different tasks? y/n - ")
            if prompt2 == "y":
                for row in c.execute("SELECT DISTINCT task FROM time"):
                    print(row)
            
            # ask for intention
            prompt3 = input("what task do you want to see? - ")
            
            # print the table
            for row in c.execute("SELECT * FROM time WHERE task = '" + prompt3 + "'" ):
                 print(row)
                 
        else:
            # print the table
            for row in c.execute("SELECT * FROM time"):
                 print(row)
                 
    elif initialQuestion == "3":
                
        # ask for intention
        prompt2 = input("do you want to view predictions for a specific task? y/n - ")
        
        if prompt2 == "y":
            
            # offer reminder
            prompt3 = input("do you want to view the different tasks? y/n - ")
            if prompt3 == "y":
                for row in c.execute("SELECT DISTINCT task FROM time"):
                    print(row[0])
            
            # ask for intention
            prompt4 = input("what task do you want to see averages for? - ")
            
            # show predictions
            predict(prompt4)
            
        else:
            
            # show predictions for all distinct tasks
            tasks = []
            for row in c.execute("SELECT DISTINCT task FROM time"):
                tasks.append(row[0])
            for i in tasks:
                print(predict(i))
            
    elif initialQuestion == "4":
        
        test = input("h:m:s - ")
        print("to unix - " + str(toUnix(test)))
        print("to time - " + str(toTime(test)))
        
    else:
        break

#---------#
#-- End --#
#---------#

# Commit all changes to the database and close the connection
connection.commit()   # Save (commit) the changes:
connection.close()    # Close the connection
