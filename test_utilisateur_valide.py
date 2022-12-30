import unittest
from utilisateur_valide import user_is_valid

class TestUtilisateurs(unittest.TestCase):
	
	def test_user_is_valid(self):
		#Utilisateur et mot de passe valides et dans la base de données
		self.assertEqual(user_is_valid('frede','1M!tdePasse'),True)
		self.assertTrue(user_is_valid('user','@S@fePassword12'))
		#Utilisateur/mdp valide mais pas dans la base de données
		self.assertFalse(user_is_valid('baptiste','1M!tdePasse'))        
		self.assertFalse(user_is_valid('baptiste','@ZertyTest123'))
		#Utilisateur invalide
		self.assertFalse(user_is_valid('fr','1Mo!deP@sse'))
		#Mot de passse invalide
		self.assertEqual(user_is_valid('baptiste','@ZertyTest'),False)


if __name__ == '__main__':
    unittest.main()





