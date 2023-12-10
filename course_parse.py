import sqlite3

with open("course.txt", "r+") as fi:
    lines = fi.readlines()

# Connect to DB and create a cursor
db = sqlite3.connect('instance/database.db')
c = db.cursor()
print('DB Init')

for line in lines:
    c.execute('INSERT INTO course (course_number) VALUES (?)', (line.replace("\n", ""),))
    db.commit()
 
# Close the cursor
c.close()