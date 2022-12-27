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

conn.commit()