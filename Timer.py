# This Python file uses the following encoding: utf-8

### Import Modules ###
import sqlite3 # databases

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

#def mean():
    # calculates the mean
    # = sum()/count()


#def stanDev():
    # calculates the standard deviation
    # sd = sqrt (sum(|x-x\bar|^2)/n)

while True:
    
    # ask for intention
    question = input("Do you want to log a time? y/n - ")
    if question == "y":
        
        # ask for inputs
        typeQuestion = input("What type of task was it? e.g. Travel/Prep/Housework - ")
        taskQuestion = input("What task do you want to log? e.g. Travelling to uni -  ")
        timeQuestion = input("How long did it take you? [hh]:mm:ss - ")
        print("Type: " + typeQuestion + "\nTask: " + taskQuestion + "\nQuestion: " + timeQuestion)

        # add the inputs to the database
        logArr = [typeQuestion, taskQuestion, timeQuestion]
        c.execute("INSERT INTO time VALUES (?,?,?)", logArr)

        # commit changes
        connection.commit()
        
    else:
        # ask for intention
        question2 = input("do you want to view your current logs? y/n - ")
        if question2 == "y":
            
            # Print sources of income
            print("Your sources of spending are:")
            for row in c.execute("SELECT * FROM time"):
	            print(row)
        break

#---------#
#-- End --#
#---------#

# Commit all changes to the database and close the connection
connection.commit()   # Save (commit) the changes:
connection.close()    # Close the connection
