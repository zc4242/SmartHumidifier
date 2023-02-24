from fastapi import FastAPI
import sqlite3
import datetime
from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    room: Union[str, None] = None
    temperature: float
    humidity: float


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/status/ethan")
async def get_status():
    connection = sqlite3.connect('status.db',
                                 detect_types=sqlite3.PARSE_DECLTYPES |
                                              sqlite3.PARSE_COLNAMES)
    # cursor = connection.cursor()

    # q="SELECT DateTime, Temperature, Humidity, Room FROM status"

    q = '''SELECT *     
    FROM status T1    
    WHERE DateTime = (
    SELECT max(DateTime)
    FROM status T2
    WHERE T2.Room = 'Ethan room'
    )'''
    my_cursor = connection.execute(q)

    data_row = my_cursor.fetchone()
    print(type(data_row))  # <class 'tuple'>
    record_time = data_row[0]
    print(record_time)
    result = {
        "temperature": data_row[1],
        "humidity": data_row[2]
    }
    print(result)
    # return {
    #         "temperature": 25.8,
    #         "humidity": 38
    #         }

    # get the current datetime and store it in a variable
    currentDateTime = datetime.datetime.now()
    print(currentDateTime)
    record_time = data_row[0]
    print(record_time)
    time_delta_minutes = (currentDateTime - record_time).total_seconds() / 60

    if time_delta_minutes > 10:
        # result = {
        #         "temperature": 0,
        #         "humidity": 0
        #         }
        return None
    return result


@app.get("/status/main")
async def get_status():
    connection = sqlite3.connect('status.db',
                                 detect_types=sqlite3.PARSE_DECLTYPES |
                                              sqlite3.PARSE_COLNAMES)
    # cursor = connection.cursor()

    # q="SELECT DateTime, Temperature, Humidity, Room FROM status"

    q = '''SELECT *     
    FROM status T1    
    WHERE DateTime = (
    SELECT max(DateTime)
    FROM status T2
    WHERE T2.Room = 'Main room'
    )'''
    my_cursor = connection.execute(q)

    data_row = my_cursor.fetchone()
    print(type(data_row))  # <class 'tuple'>
    record_time = data_row[0]
    print(record_time)
    result = {
        "temperature": data_row[1],
        "humidity": data_row[2]
    }
    print(result)
    # return {
    #         "temperature": 25.8,
    #         "humidity": 38
    #         }

    # get the current datetime and store it in a variable
    currentDateTime = datetime.datetime.now()
    print(currentDateTime)
    record_time = data_row[0]
    print(record_time)
    time_delta_minutes = (currentDateTime - record_time).total_seconds() / 60

    if time_delta_minutes > 10:
        # result = {
        #         "temperature": 0,
        #         "humidity": 0
        #         }
        # # return None
        return None
    return result


@app.get("/last_status")
async def get_status():
    connection = sqlite3.connect('status.db',
                                 detect_types=sqlite3.PARSE_DECLTYPES |
                                              sqlite3.PARSE_COLNAMES)
    q = '''SELECT *     
    FROM status T1    
    WHERE DateTime = (
    SELECT max(DateTime)
    FROM status T2
    )'''
    my_cursor = connection.execute(q)
    data_row = my_cursor.fetchone()
    record_time = data_row[0]
    print(record_time)
    result = {
        "datetime": data_row[0],
        "temperature": data_row[1],
        "humidity": data_row[2]
    }
    print(result)
    return result


@app.post("/update/ethan")
async def update_status(item: Item):
    currentDateTime = datetime.datetime.now()
    print(currentDateTime)
    # make the database connection with detect_types
    connection = sqlite3.connect('status.db',
                                 detect_types=sqlite3.PARSE_DECLTYPES |
                                              sqlite3.PARSE_COLNAMES)
    cursor = connection.cursor()

    # create query to insert the data
    insertQuery = """INSERT INTO STATUS
        VALUES (?, ?, ?, ?);"""

    # insert the data into table
    cursor.execute(insertQuery, (currentDateTime, item.temperature, item.humidity - 10, item.room
                                 ))
    # cursor.execute(insertQuery, (2, "Rohit Pathak",

    print("Data Inserted Successfully !")

    # commit the changes,
    # close the cursor and database connection
    connection.commit()
    cursor.close()
    connection.close()


@app.post("/update/main")
async def update_status(item: Item):
    currentDateTime = datetime.datetime.now()
    print(currentDateTime)
    # make the database connection with detect_types
    connection = sqlite3.connect('status.db',
                                 detect_types=sqlite3.PARSE_DECLTYPES |
                                              sqlite3.PARSE_COLNAMES)
    cursor = connection.cursor()

    # create query to insert the data
    insertQuery = """INSERT INTO STATUS
        VALUES (?, ?, ?, ?);"""

    # insert the data into table
    cursor.execute(insertQuery, (currentDateTime, item.temperature, item.humidity - 10, item.room
                                 ))
    # cursor.execute(insertQuery, (2, "Rohit Pathak",

    print("Data Inserted Successfully !")

    # commit the changes,
    # close the cursor and database connection
    connection.commit()
    cursor.close()
    connection.close()
