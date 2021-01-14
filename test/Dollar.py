from Money import Money

class Dollar(Money):
    
    def __init__(self, amount):
        Money.__init__(self, amount)
        self.currency = 'USD'