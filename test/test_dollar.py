from Dollar import Dollar
 
def test_multiplication():
    assert Dollar(10).amount == Dollar(5).times(2) 
    assert Dollar(15).amount == Dollar(5).times(3) 
    
    
def test_equality():
    assert Dollar(5).equals(Dollar(5))     
    assert False == Dollar(5).equals(Dollar(4))


def test_dollar():
    assert Dollar(4).equals(Dollar(4))