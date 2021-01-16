from Money import Money
from Franc import Franc
from Dollar import Dollar


def test_dollar():
    assert Dollar(10).equals_currency(Dollar(10))
    assert Dollar(10).equals_currency(Dollar(15))
    
    
def test_franc():
    assert Franc(10).equals_currency(Franc(10))
    assert Franc(10).equals_currency(Franc(15))
    

def test_money():
    assert Money(10).equals_currency(Money(10))
    assert Money(10).equals_currency(Money(15))
    

def test_inter():
    assert False == Dollar(10).equals_currency(Franc(10))
    assert False == Dollar(10).equals_currency(Franc(15))
    
    assert False == Money(10).equals_currency(Franc(10))
    assert False == Money(10).equals_currency(Franc(15))