class Money(object):
    
    def __init__(self, amount):
        self.amount = amount 
        self.currency = '$'
    
        
    def equals(self, object) -> bool:
        try:
            return self.amount == object.amount
        except:
            print('Error: Object is not a Money')
    
    
    def equals_currency(self, object):
        try:
            return self.currency == object.currency
        except:
            print('Error: Object is not a Money')       



    def money(self, amount) -> None:
        self.amount = amount


    def times(self, multiplier):        
        return (self.amount * multiplier)
    
    
    def dollar(self, dollar):
        return dollar
    
    
    @property
    def amount(self):
        return self._amount 
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount
        
    @amount.deleter
    def amount(self):
        del self._amount
        
        
    @property
    def currency(self):
        return self._currency 
    
    
    @currency.setter
    def currency(self, currency):
        self._currency = currency

        
    @currency.deleter
    def currency(self):
        del self._currency