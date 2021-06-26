#!/usr/bin/env python
""" Franc coin """

from . import Money


class Franc(Money):
    
    def __init__(self, amount):
        Money.__init__(self, amount)
        self.exchange_rate = 0.5
        self.currency = 'CHF'