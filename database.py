import sqlite3

conn = sqlite3.connect('people.db')
cur = conn.cursor()
cur.execute('SELECT * FROM person ORDER BY fname')
people = cur.fetchall()
for person in people:
    print(person[3],f'{person[2]} {person[1]}', person[4], person[5], person[6] )

cur.execute('SELECT * FROM user ORDER BY username')
user  = cur.fetchall()
for u in user:
    print (u[1], u[2])