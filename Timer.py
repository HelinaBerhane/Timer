# This Python file uses the following encoding: utf-8

### Import Modules ###
import sqlite3 # databases

#--------------------#
#-- Initialisation --#
#--------------------#

# create the connection object that represents the database
connection = sqlite3.connect('budget.db')
# create a Cursor object and call its execute() method to perform SQL commands:
c = connection.cursor()
# Create the tables
c.execute("CREATE TABLE IF NOT EXISTS time(type STRING(50), task STRING(100), time FLOAT, notes STRING(1000))")

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
    Question = input("Do you want to log a time? y/n: ")
    if Question == "y":
        typeQuestion = input("What type of task was it? e.g. Travel/Prep/Housework - ")
        taskQuestion = input("What task do you want to log? e.g. Travelling to uni -  ")
        timeQuestion = input("How long did it take you? [hh]:mm:ss - ")
        print("Type: " + typeQuestion + ". Task: " + taskQuestion + ". Question: " + timeQuestion)
    else:
        break

#---------#
#-- End --#
#---------#

# Commit all changes to the database and close the connection
connection.commit()   # Save (commit) the changes:
connection.close()    # Close the connection
