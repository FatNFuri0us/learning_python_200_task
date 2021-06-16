# -*- coding: utf-8 -*-
"""
asserEqual - sprawdz czy 2 elementy sa rowne
assertNotEqual -sprawdza czy 2 elementy nie sa rowne
assertTrue - sprawdza czy wyrazenie / element jest prawda
assertFalse - sprawdza czy wyrazenie / element jest falszem
assertIn - sprawdza przynaleznosc (cz nalezy)
assertNotIn - sprawdzwa przynaleznosc (cz nie nalezy)

"""
# %%
import unittest


class SimpleTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(3 + 7, 11)
        
    def test_sub(self):
        self.assertNotEqual(8 - 3, 5)
        
    def test_true(self):
        self.assertTrue(3 + 7 == 10)
        
    def test_false(self):
        self.assertFalse(3 + 7 == 11)
        
    def test_in(self):
        self.assertIn(3, [1, 2, 3, 4])
        
    def test_not_in(self):
        self.assertNotIn(20, range(15))
        
if __name__ == '__main__': 
    unittest.main()       
        
        
        
        
        
        
        
        
        
        
        
        