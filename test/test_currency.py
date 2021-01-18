import unittest

from Financial import Money, Franc, Dollar


class Test_Currency(unittest.TestCase):

    def test_dollar(self):
        assert Dollar(10).equals_currency(Dollar(10))
        assert Dollar(10).equals_currency(Dollar(15))
        
        
    def test_franc(self):
        assert Franc(10).equals_currency(Franc(10))
        assert Franc(10).equals_currency(Franc(15))
        

    def test_money(self):
        assert Money(10).equals_currency(Money(10))
        assert Money(10).equals_currency(Money(15))
        

    def test_inter(self):
        self.assertFalse(Dollar(10).equals_currency(Franc(10)))
        self.assertFalse(Dollar(10).equals_currency(Franc(15)))
        
        self.assertFalse(Money(10).equals_currency(Franc(10)))
        self.assertFalse(Money(10).equals_currency(Franc(15)))