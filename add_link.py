import sqlite3
#Open database
conn = sqlite3.connect('utilisateurs.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()


def user_is_valid(username,password):
   
   l, u, s, d = 0, 0, 0, 0
   capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   smallalphabets="abcdefghijklmnopqrstuvwxyz"
   specialchar='""!@#$%^&*()-+?_=,<>/""'
   digits="0123456789"

   if (len(username) >= 3):
       for i in username:
           # vérifier s'il y a des caractères spéciaux dans le username
           if(i in specialchar):
               return False 
   else:
      return False 

   if (len(password) >= 8):
       for i in password:
    
           # compter les lettres minuscules
           if (i in smallalphabets):
               l+=1           
    
           # compter les lettres majuscules
           if (i in capitalalphabets):
               u+=1           
    
           # compter les chiffres
           if (i in digits):
               d+=1           
    
           # compter les caractères spéciaux
           if(i in specialchar):
               s+=1       
               
   if (l>=1 and u>=1 and s>=1 and d>=1 and l+s+u+d==len(password)):
      #Vérifier si l'utilisateur appartient à la base de données
      for raw in c.execute('SELECT * FROM  Utilisateurs'):
         if raw["Username"] == username and raw["Password"] == password:
            print("Valid user")
            return True
   else:
       print("Invalid user")
       return False

def add_link(username,password,link):
   #vérifier si l'utilisateur existe et si le couple username/password est valide
   if not(user_is_valid(username,password)):
      print("Invalid user")
      return False

   id_user = c.execute("SELECT id FROM Utilisateurs WHERE Username = (?) AND Password = (?)",[username,password]).fetchone()
   id_user=id_user['id']
   c.execute("INSERT INTO  Liens(Link,Id_utilisateur) VALUES (?,?)",[link,id_user])

   
   id_link = c.execute("SELECT id FROM Liens WHERE Link = (?)",[link]).fetchone()
   id_link=id_link['id']

   print(id_user,id_link)
   c.execute("INSERT INTO  Utilisateur_possede_lien VALUES (?,?)",[id_user,id_link])

   links = c.execute("SELECT * FROM Liens WHERE Id_utilisateur = (?)",[id_user]).fetchall()

   tab_links=[]
   for i in range(len(links)):
      tab_links.append(links[i]['link'])

   print(tab_links)
   if(link in tab_links):
      print("Success")
      return True
   else:
      print("Failed to add link")
      return False



#Close database
conn.commit()


