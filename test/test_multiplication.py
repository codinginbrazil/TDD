from Financial import Money, Franc, Dollar


def test_dollar():
    assert Dollar(10).amount == Dollar(5).times(2) 
    assert Dollar(15).amount == Dollar(5).times(3) 
    
    
def test_franc():
    assert Franc(10).amount == Franc(5).times(2) 
    assert Franc(15).amount == Franc(5).times(3) 
    
def test_money():
    assert Money(10).amount == Money(5).times(2) 
    assert Money(15).amount == Money(5).times(3) 