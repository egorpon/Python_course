import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE FRIENDS (firs_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO FRIENDS VALUES ('Ivan','Tkachenko',4)'''

# DONT DO THIS!
# form_first = "Dana"
# query = f"INSERT INTO FRIENDS (firs_name) VALUES ('{form_first}')"

# BETTER WAY!
# form_first = "Mary-Todd"
# query = "INSERT INTO FRIENDS (firs_name) VALUES (?)"
# c.execute(query,(form_first,))

# TOP METHOD!
# data = ("Steve", "Irwin", 9)
# query = "INSERT INTO FRIENDS VALUES (?,?,?)"
# c.execute(query,data)

# commit changes
conn.commit()
conn.close()