import sqlite3
def dbQuery(database, command):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(command)  # retreive and return from the database.
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result