from src.Dollar import Dollar

d = Dollar()

def test_multiplication():
    d.dollar(5)
    d.times(3)
    assert d.amount == 15