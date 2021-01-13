from Franc import Franc


def test_multiplication():
    assert Franc(10).amount == Franc(5).times(2) 
    assert Franc(15).amount == Franc(5).times(3) 