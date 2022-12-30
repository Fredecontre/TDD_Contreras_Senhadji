import unittest
from add_link import add_link

class TestAddLink(unittest.TestCase):

    def test_add_link(self):
        #Ajouts de lien corrects
        self.assertEqual(add_link('frede','1M!tdePasse','unlink'),True)
        self.assertEqual(add_link('user','@S@fePassword12','helloworld'),True)
        #A ce stade du développement, même un mauvais link est rajouté
        #car la véritication est fait dans la feature verify_links
        self.assertTrue(add_link('frede','1M!tdePasse','m@ava!s_link'))
        #Ajout de lien pour utilisateur qui n'existe pas, renvoie erreur
        self.assertFalse(add_link('unknownuser','1M!tdePasse','mylink'))
            

if __name__ == '__main__':
    unittest.main()
