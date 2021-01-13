from Franc import Franc


def test_multiplication():
    five = Franc(5)
    
    assert Franc(10).amount == five.times(2) 
    assert Franc(15).amount == five.times(3) 