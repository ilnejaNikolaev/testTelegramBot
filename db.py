import random
import sqlite3


connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)  
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#cursor.execute("INSERT INTO Users (username,email,age) VALUES (?,?,?)", ("username", "ex@gmail.com","28"))
#for i in range(30):
 #   cursor.execute("INSERT INTO Users (username,email,age) VALUES (?,?,?)", (f"username{i}", f"{i}ex@gmail.com",str(random.randint(28,60))))
#cursor.execute("UPDATE Users SET age = ? WHERE username = ?",(29,"newuser"))
#cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser",))

cursor.execute("SELECT * FROM Users")
# SELECT FROM WHERE GROUP BY HAVING ORDER BY

#cursor.execute("SELECT username FROM Users WHERE age > ?", (50,))

cursor.execute("SELECT age , AVG(age) FROM Users GROUP BY age")

users = cursor.fetchall()
for user in users:
    print(user)
connection.commit()
connection.close()
