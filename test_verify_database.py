import unittest
from verify_database import verify_database, add_link,add_user

class TestUtilisateurs(unittest.TestCase):

    def test_get_links(self):
        #Exemples corrects
        self.assertEqual(verify_database(),True)
        add_link('frede','1M!tdePasse','unlink')
        self.assertTrue(verify_database())
        add_user('validuser','B@nM0tDePasse')
        self.assertTrue(verify_database())
        
        #Ajout d'un lien invalide et vérification que la fonction returne False
        add_link('user','@S@fePassword12','l!ien inv@lide')
        self.assertFalse(verify_database())

        #Ajout d'un utilisateur invalide et vérification que la fonction returne False
        add_user('aa','m)dpasse_pasn@n')
        self.assertEqual(verify_database(),False)
    

if __name__ == '__main__':
    unittest.main()