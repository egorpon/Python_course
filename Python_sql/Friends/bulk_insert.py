import sqlite3

conn = sqlite3.connect("my_friends.db")
# create a cursor object
c = conn.cursor()

people = [
    ("Roald","Amundsen",5),
    ("Linda","Pogel",7),
    ("Mark","Beckler",9),
    ("Jacob","Swarowcki",3),
    ("Daniel","Mickew",6)
]



# c.executemany("INSERT INTO FRIENDS VALUES (?,?,?)",people)

for person in people:
    c.execute("INSERT INTO FRIENDS VALUES (?,?,?)",person)
    print("INSERTING NOW!!!")

# c.execute()
# commit changes
conn.commit()
conn.close()