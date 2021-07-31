import sqlite3

#connecting database
mov = sqlite3.connect('favmovies.db')

#creating cursor
c = mov.cursor()

#query the database by lead actor name
c.execute("SELECT * FROM movies WHERE lead_actor = 'TOM CRUISE' ")

# # prints all TOM CRUISE's movies
# print(c.fetchall())

#prints all TOM CRUISE's movies line by line
items = c.fetchall()

for item in items:
    print(item) 


#commit commaands
mov.commit()

#close connections
mov.close()
