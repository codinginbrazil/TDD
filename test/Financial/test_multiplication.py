import unittest

from Financial import Money, Franc, Dollar

class Test_Multiplication(unittest.TestCase):
    
    def test_dollar(self):
        self.assertEqual(Dollar(10).amount, Dollar(5).times(2))
        self.assertEqual(Dollar(15).amount, Dollar(5).times(3))
        
        
    def test_franc(self):
        self.assertEqual(Franc(10).amount, Franc(5).times(2)) 
        self.assertEqual(Franc(15).amount, Franc(5).times(3)) 
        
        
    def test_money(self):
        self.assertEqual(Money(10).amount, Money(5).times(2)) 
        self.assertEqual(Money(15).amount, Money(5).times(3)) 