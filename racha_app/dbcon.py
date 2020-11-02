import json
import mysql.connector
from mysql.connector import Error      

def connect(file):
    
    with open(file) as json_file:
        parameters = json.load(json_file)

    connection = mysql.connector.connect(
        host = parameters['host'],
        database = parameters['database'],
        user = parameters['user'],
        password = parameters['password']
    )

    cursor = connection.cursor()
    
    return cursor, connection