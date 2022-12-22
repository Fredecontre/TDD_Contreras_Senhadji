import unittest
from verify_database import verify_database

class TestUtilisateurs(unittest.TestCase):

    def test_add_user(self):
        self.assertEqual(verify_database(),True)
        # self.assertTrue(verify_database())
        # #A ce stade du dévéloppement, les utilisateurs/mdp invalides sont quand même ajoutés à
        # # la base de données
        # self.assertFalse(not(verify_database()))
        # self.assertEqual(verify_database(),True)

if __name__ == '__main__':
    unittest.main()