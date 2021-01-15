from Money import Money
from Franc import Franc
from Dollar import Dollar


class Bank(object):
    
    def __init__(self):
        pass
    

    def exchange_rate(self, coin):
        return round(coin.amount * coin.exchange_rate, 3)
        
        
    def source_to_destiny(self, source, destiny):
        source = self.exchange_rate(source) 
        if destiny == 'USD':
            return source / Dollar(0).exchange_rate
        elif destiny == 'CHF':
            return source / Franc(0).exchange_rate
        else:
            return False
        
            
    def reduced(self, coin):
        if coin.currency == 'USD':
            return coin.amount
        elif coin.currency == 'CHF':
            return coin.amount
        elif coin.currency == '$':
            return coin.amount
        else: 
            return('Error: Currency not found')
        
        