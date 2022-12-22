import unittest
from get_links import get_links

class TestUtilisateurs(unittest.TestCase):

    def test_get_links(self):
        #Exemples corrects
        self.assertEqual(get_links('frede','1M!tdePasse'),['deffunction','deffunction2'])
        self.assertTrue(get_links('user','@S@fePassword12')==[])
        
        #Utilisateur/mot de passse incorrect
        self.assertFalse(get_links('fr','1Mo!deP@sse'))
        self.assertEqual(get_links('baptiste','@S@fePassword12'),False)
        self.assertFalse(get_links('frederiiiick','1M!tdePasse'))


if __name__ == '__main__':
    unittest.main()