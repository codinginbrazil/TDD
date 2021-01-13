import logging

from src.Dollar import Dollar


logging.basicConfig(filename=('log/test_dollar.txt'),
                    level=logging.DEBUG, 
                    format=' %(asctime)s - %(levelname)s - %(message)s')

# logging.disable()
logging.debug('Start of program')
    
    
def test_multiplication():
    five = Dollar(5)
    
    assert 10 == five.times(2)
    assert 15 == five.times(3)
    
    logging.debug('     test_multiplication     ')
    logging.debug(five.times(2))
    logging.debug('10 is equal 10: ' + str(10 == five.times(2)))
    logging.debug(five.times(3))
    logging.debug('10 is equal 10: ' + str(15 == five.times(3)))
    
def test_equality():
    five = Dollar(5)
    four = Dollar(5)
    assert five.equals(four)     
    
    four.dollar(4)
    assert False == five.equals(four)
