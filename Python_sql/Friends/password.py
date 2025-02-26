import sqlite3

conn = sqlite3.connect("users.db")

c = conn.cursor()
# query ="CREATE TABLE users (username TEXT, password TEXT);"
u = input("please enter ur username... ")
p = input("please enter ur password... ")

query  = "select * from users Where username =? and password = ?"
c.execute(query,(u,p))

result = c.fetchone()
if result:
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")

conn.commit()
conn.close()