import sqlite3
import datetime

# get the current datetime and store it in a variable
currentDateTime = datetime.datetime.now()

# make the database connection with detect_types
connection = sqlite3.connect('status.db',
                             detect_types=sqlite3.PARSE_DECLTYPES |
                                          sqlite3.PARSE_COLNAMES)

q = '''SELECT *     
FROM status T1    
WHERE DateTime = (
   SELECT max(DateTime)
   FROM status T2
   WHERE T2.Room = 'Main room'
)'''
my_cursor = connection.execute(q)

data_row = my_cursor.fetchone()
print(type(data_row))
result = {"0": data_row[0],
          "temperature": data_row[1],
          "humidity": data_row[2],
          "3": data_row[3]
          }
print(result)
record_time = data_row[0]
print(record_time)

time_delta = currentDateTime - record_time
print('Difference: ', time_delta)

time_delta_minutes = time_delta.total_seconds() / 60
print('Total difference in minutes: ', time_delta_minutes)
