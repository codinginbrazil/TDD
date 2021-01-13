class Money(object):
    
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
            print('Error: Object is not a Dollar')


    def dollar(self, amount) -> None:
        self.amount = amount


    def times(self, multiplier):        
        return (self.amount * multiplier)