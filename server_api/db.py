import datetime
import sqlite3

# get the current datetime and store it in a variable
currentDateTime = datetime.datetime.now()

# make the database connection with detect_types
connection = sqlite3.connect('status.db',
                             detect_types=sqlite3.PARSE_DECLTYPES |
                                          sqlite3.PARSE_COLNAMES)
cursor = connection.cursor()

# create table in database
createTable = '''CREATE TABLE STATUS (
    DateTime TIMESTAMP,
    Temperature NUMERIC,
    Humidity NUMERIC,
    Room VARCHAR(30));'''
cursor.execute(createTable)

# create query to insert the data
insertQuery = """INSERT INTO STATUS
    VALUES (?, ?, ?, ?);"""

# insert the data into table
cursor.execute(insertQuery, (currentDateTime, 68, 45.2, "Name of Room"
                             ))

print("Data Inserted Successfully !")

# commit the changes,
# close the cursor and database connection
connection.commit()
cursor.close()
connection.close()
