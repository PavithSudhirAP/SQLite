import sqlite3

#connecting database
mov = sqlite3.connect('favmovies.db')

#creating cursor
c = mov.cursor()


#Add single data
# c.execute("INSERT INTO movies VALUES ('Mr. Nobody','Jared Leto','Diane Kruger','2009','Jaco Van Dormael')")


#Add multiple data
movie_list = [
              ('MR. NOBODY','JARED LETO','DIANE KRUGER','2009','JACO VAN DORMAEL'),
              ('AVATAR', 'SAM WORTHINGTON','ZOE SALDANA','2009','JAMES CAMERON'),
              ('DIE HARD','BRUCE WILLIS','BONNIE BEDELIA','1988','JOHN MCTIERNAN'),
              ('JOHN WICK','KEANU REEVES','BRIDGET MOYNAHAN','2014','CHAD STAHELSKI'),
              ('INTERSTELLAR','MATTHEW MCCONAUGHEY','ANNE HATHAWAY','2014','CHRISTOPHER NOLAN'),
              ('HOW TO TRAIN YOUR DRAGON','JAY BARUCHEL','AMERICA FERRER','2010','DEAN DEBLOIS'),
              ('PREDESTINATION','ETHAN HAWKE','SARAH SNOOK','2014','MICHAEL SPIERIG'),
              ('EDGE OF TOMORROW','TOM CRUISE','EMILY BLUNT','2014','DOUG LIMAN'),
              ('KINGSMAN: THE SECRET SERVICE','TARON EGERTON','HANNA ALSTROM','2014','MATTHEW VAUGHN'),
              ('INCEPTION','LEONARDO DICAPRIO','MARION COTILLARD','2010','CHRISTOPHER NOLAN'),
              ('SPIDER-MAN','TOBEY MAGUIRE','KIRSTEN DUNST','2002','SAM RAIMI'),
              ('MEMENTO','GUY PEARCE','CARRIE-ANNE MOSS','2000','CHRISTOPHER NOLAN'),
              ('I, ROBOT','WILL SMITH','BRIDGET MOYNAHAN','2004','ALEX PROYAS'),
              ('THE HANGOVER','BRADLEY COOPER','HEATHER GRAHAM','2009','TODD PHILLIPS'),
              ('MISSION: IMPOSSIBLE - FALLOUT','TOM CRUISE','REBECCA FERGUSON','2018','CHRISTOPHER MCQUARRIE'),
              ('JURASSIC PARK','SAM NEILL','LAURA DERN','1993','STEVEN SPIELBERG'),
              ('VENOM','TOM HARDY','MICHELLE WILLIAMS','2018','RUBEN FLEISCHER'),
              ]

c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", movie_list )
 

#commit commaands
mov.commit()

#close connections
mov.close()
