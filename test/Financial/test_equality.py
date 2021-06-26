#!/usr/bin/env python
"""Test for the money.equals module."""

import unittest

from Financial import Money, Franc, Dollar


class Test_Equality(unittest.TestCase):
    def test_dollar(self):
        assert Dollar(4).equals(Dollar(4))    
        assert Dollar(5).equals(Dollar(5))
        
        self.assertFalse(Dollar(5).equals(Dollar(4)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))
        
        
    def test_franc(self):
        assert (Franc(5).equals(Franc(5)))
        self.assertFalse(Franc(5).equals(Franc(6)))


    def test_money(self):
        assert Money(4).equals(Money(4))    
        assert Money(5).equals(Money(5))
        
        self.assertFalse(Money(5).equals(Money(4)))
        self.assertFalse(Money(5).equals(Money(6)))


    def test_inter(self):
        self.assertFalse(Dollar(5).equals(Franc(5)))
        self.assertFalse(Dollar(5).equals(Franc(6)))


if __name__ == '__main__':
    unittest.main()