import sqlite3

conn = sqlite3.connect('people.db')
cur = conn.cursor()
cur.execute('SELECT * FROM person ORDER BY lname')
people = cur.fetchall()
for person in people:
    print(person[3],f'{person[2]} {person[1]}', person[4], person[5], person[6] )