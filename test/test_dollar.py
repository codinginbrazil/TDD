import logging

from Dollar import Dollar


logging.basicConfig(filename=('log/test_dollar.txt'),
                    level=logging.DEBUG, 
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable()
logging.debug('Start of program')
 
 
def test_multiplication():
    five = Dollar(5)
    
    assert Dollar(10).amount == five.times(2) 
    assert Dollar(15).amount == five.times(3) 
    
    
def test_equality():
    five = Dollar(5)
    four = Dollar(5)
    assert five.equals(four)     
    
    four.dollar(4)
    assert False == five.equals(four)


def test_dollar():
    four = Dollar(6)
    four.dollar(4)
    
    assert four.equals(Dollar(4))