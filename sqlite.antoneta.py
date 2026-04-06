import sqlite3

db = sqlite3.connect("python_programming.db") # create db
cursor = db.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS python_programming(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               grade INTEGER NOT NULL)
               ''')
db.commit()

student_info= [
             (55, "Carl Davis", 61),
            (66, "Dennis Fredrickson", 88),
            (77, "Jane Richards", 78), 
            (12, "Peyton Sawyer", 45), 
            (2, "Lucas Brooke", 99)
            ]

 # need many here as you are doing a number of inserts
 # add OR IGNORE TO so you do not have error if you run this multiple times
cursor.executemany(''' 
            INSERT OR IGNORE Into python_programming(id, name, grade)
            VALUES(?, ?, ?)
            ''', student_info)
db.commit()


cursor.execute('''
            SELECT id, name, grade 
            FROM python_programming
            WHERE grade between ? and ?''', (60, 80))

print("\nStudents with grades between 60 and 80: ")
for row in cursor.fetchall():
    print(row)

cursor.execute('''
               UPDATE python_programming 
               Set grade = ? 
               Where id = ?
               ''', (65, 55))

db.commit()

cursor.execute(''' 
               DELETE FROM python_programming 
               WHERE id = ?
               ''', (66,)) # a comma is needed after 66
db.commit()

cursor.execute('''
                UPDATE python_programming 
               SET grade = ? 
               WHERE id >= ?
                ''', (80, 55))

# Select and print all records from the table to see the final results
cursor.execute('''
              SELECT * 
               FROM python_programming
''')
final_results = cursor.fetchall()
print('\nFinal results:')
for row in final_results:
    print(row)

db.commit()

db.close()