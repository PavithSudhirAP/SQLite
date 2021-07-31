import sqlite3

#connecting database
mov = sqlite3.connect('favmovies.db')

#creating cursor
c = mov.cursor()

#creating table
c.execute("""CREATE TABLE movies (
        movie_name text,
        lead_actor text,
        actress text,
        release_year text,
        director text    
    )""")

#commit commaands
mov.commit()

#close connections
mov.close()
