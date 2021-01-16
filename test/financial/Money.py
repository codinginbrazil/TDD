class Money(object):
    
    def __init__(self, amount):
        self.amount = amount 
        self.currency = '$'
    
    
    def __repr__(self):
        return (str(self.currency) + ' ' + str(self.amount))    


    def money(self, amount) -> None:
        self.amount = amount


    def times(self, multiplier):        
        return (self.amount * multiplier)
    
    
    def plus(self, addend):
        # [OFF] Curiosity: sum = augend + addend + addend
        return self.amount + addend
    
    
    def equals(self, thing) -> bool:
        try:
            return self.equals_amount(thing) and self.equals_currency(thing)
        except:
            print('Error: Object is not a Money')
    
    def equals_amount(self, thing) -> bool:
        try:
            return self.amount == thing.amount
        except:
            print('Error: Object is not a Money')
    
    def equals_currency(self, thing):
        try:
            return self.currency == thing.currency
        except:
            print('Error: Object is not a Money')   
    
    
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
        
    
    @property
    def exchange_rate(self):
        return self._exchange_rate 
    
    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        self._exchange_rate = exchange_rate
  
    @exchange_rate.deleter
    def exchange_rate(self):
        del self._exchange_rate