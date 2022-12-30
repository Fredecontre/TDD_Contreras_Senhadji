import unittest
from ajout_utilisateur import add_user 

class TestUtilisateurs(unittest.TestCase):

    def test_add_user(self):
        self.assertEqual(add_user('frederick','1Mo!deP@sse'),True)
        self.assertTrue(add_user('baptiste','@ZertyTest123'))
        
        #A ce stade du dévéloppement, les utilisateurs/mdp invalides sont quand même 
        # censés être ajoutés à la base de données
        self.assertFalse(not(add_user('fr','1Mo!deP@sse')))
        self.assertEqual(add_user('baptiste','@ZertyTest'),True)


if __name__ == '__main__':
    unittest.main()
