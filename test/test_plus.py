from Financial import Money, Franc, Dollar, Bank


def test_dollar():
    assert Dollar(7).amount == Dollar(5).plus(2) 
    assert Dollar(8).amount == Dollar(5).plus(3) 
    
    
def test_franc():
    assert Franc(7).amount == Franc(5).plus(2) 
    assert Franc(8).amount == Franc(5).plus(3) 

    
def test_money():
    assert Money(7).amount == Money(5).plus(2) 
    assert Money(8).amount == Money(5).plus(3) 
    
    
def test_simples():
    assert Money(10).amount == Bank().reduced(Money(
        Money(5).plus(5)))

