import sqlite3
#Open database
conn = sqlite3.connect('utilisateurs.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()


def add_user(username,password):
   

   c.execute("INSERT INTO  Utilisateurs(Username,Password) VALUES (?, ?)",[username,password])

   #Vérifier si l'utilisateur a bien été rajouté dans la base de données et retourner True si c'est le cas
   for raw in c.execute('SELECT * FROM  Utilisateurs'):
      if raw["Username"] == username and raw["Password"] == password:
         print("Successfully added user to database")
         return True

   print("Fail")

conn.commit()