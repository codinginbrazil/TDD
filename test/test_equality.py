from Money import Money
from Franc import Franc
from Dollar import Dollar


def test_dollar():
    assert Dollar(4).equals(Dollar(4))    
    assert Dollar(5).equals(Dollar(5))
    
    assert False == Dollar(5).equals(Dollar(4))
    assert False == Dollar(5).equals(Dollar(6))
    
    
def test_franc():
    assert (Franc(5).equals(Franc(5)))
    
    assert False == Franc(5).equals(Franc(6))


def test_money():
    assert Money(4).equals(Money(4))    
    assert Money(5).equals(Money(5))
    
    assert False == Money(5).equals(Money(4))
    assert False == Money(5).equals(Money(6))


def test_inter():
    assert False == Dollar(5).equals(Franc(6))

