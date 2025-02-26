import sqlite3
conn = sqlite3.connect("my_friends.db")

c = conn.cursor()

c.execute("SELECT * FROM FRIENDS WHERE firs_name == 'Roald'")
c.execute("SELECT * FROM FRIENDS WHERE closeness > 5 ORDER BY closeness ASC")

# Iterate over cursor
# for result in c:
#     print(result)

#Fetch One Result
# print(c.fetchone())

# Fetch all results as list
print(c.fetchall())

conn.commit()
conn.close()