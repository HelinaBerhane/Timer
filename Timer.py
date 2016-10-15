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
c.execute("CREATE TABLE IF NOT EXISTS time(type STRING(50), task STRING(100), dailyAmount FLOAT, notes STRING(1000))")

#---------------------#
#----- Functions -----#
#---------------------#

def mean():
    # calculates the mean
    # = sum()/count()


def stanDev():
    # calculates the standard deviation
    # sd = sqrt (sum(|x-x\bar|^2)/n)


#---------#
#-- End --#
#---------#

# Commit all changes to the database and close the connection
connection.commit()   # Save (commit) the changes:
connection.close()    # Close the connection
