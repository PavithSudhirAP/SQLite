import sqlite3

#connecting database
mov = sqlite3.connect('favmovies.db')

#creating cursor
c = mov.cursor()

#query the database
c.execute("SELECT * FROM movies")

# #print everything
# print(c.fetchall()) 

#OR

#print everythin line by line
items = c.fetchall()

for item in items:
    print(item) 

#commit commaands
mov.commit()

#close connections
mov.close()
