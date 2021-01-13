from Money import Money
from Franc import Franc
from Dollar import Dollar


def test_equality():
    
    assert (Dollar(5).equals(Dollar(5)))
    assert (Franc(5).equals(Franc(5)))
    
    assert False == (Franc(5).equals(Franc(6)))
    assert False == (Dollar(5).equals(Dollar(6)))
