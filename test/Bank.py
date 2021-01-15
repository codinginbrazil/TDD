class Bank(object):
    
    def __init__(self):
       pass
        
            
    def reduced(self, coin):
        if coin.currency == 'USD':
            return coin.amount
        elif coin.currency == 'CHF':
            return coin.amount
        elif coin.currency == '$':
            return coin.amount
        else: 
            return('Error: Currency not found')
        
        