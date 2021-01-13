from Money import Money


def test_multiplication():
    five = Money(5)
    
    assert Money(10).amount == five.times(2) 
    assert Money(15).amount == five.times(3) 