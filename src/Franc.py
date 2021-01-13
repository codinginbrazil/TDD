import logging


logging.basicConfig(filename=('log/dollar.txt'),
                level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable()
logging.debug('Start of program')


class Franc(object):
    
    def __init__(self, amount):
        self.amount = amount 
    
    
    @property
    def amount(self):
        return self._amount 
    
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount
        
  
    @amount.deleter
    def amount(self):
        del self._amount
        
        
    def equals(self, object) -> bool:
        try:
            return self.amount == object.amount
        except:
            logging.WARNING('Error: Object is not a Dollar')


    def dollar(self, amount) -> None:
        self.amount = amount


    def times(self, multiplier):        
        return (self.amount * multiplier)
    
    
logging.debug('End of program')