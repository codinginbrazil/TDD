from src.Dollar import Dollar

five = Dollar(5)
    
def test_multiplication_2():
    assert 10 == five.times(2)
    
    
def test_multiplication_3():    
    assert 15 == five.times(3)