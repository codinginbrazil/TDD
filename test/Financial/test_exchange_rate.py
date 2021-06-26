#!/usr/bin/env python
"""Test for the money.amount module."""

from Financial import Money, Franc, Dollar, Bank


def test_exchange_rate():
    assert Money(5).amount == Bank().exchange_rate(Franc(10))
    assert Money(68.665).amount == Bank().exchange_rate(Franc(137.33))
    assert Money(10).amount == Bank().exchange_rate(Dollar(10))
    
    
def test_dollar_to_franc():
    assert Money(20).amount == Bank().source_to_destiny(Dollar(10), 'CHF')
    assert Money(137.33).amount == Bank().source_to_destiny(Dollar(68.665), 'CHF')
    assert Money(68.665).amount == Bank().source_to_destiny(Dollar(68.665), 'USD')

    
def test_franc_to_dollar():
    assert Money(50).amount == Bank().source_to_destiny(Franc(50), 'CHF')
    assert Money(5).amount == Bank().source_to_destiny(Franc(10), 'USD')
    assert Money(68.665).amount == Bank().source_to_destiny(Franc(137.33), 'USD')
    