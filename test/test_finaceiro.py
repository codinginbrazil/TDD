'''
    Precisamos ser capazes de somar valores em duas moedas diferentes e de
        converter o resultado, dado um conjunto de taxas de câmbio.
    Precisamos ser capazes de multiplicar um valor (preço por ação) por um
        número (número de ações) e de receber uma quantia.
'''

DOLLAR = float 


def multiplication(value,qtd):
    five = value
    five *= qtd
    return five


def test_multiplication():
    assert multiplication(3, 5) == 15
